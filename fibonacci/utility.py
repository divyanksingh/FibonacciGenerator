from fibonacci.models import Sequence


def fib(n):
    try:
        sequence = Sequence.objects.get(id = n)
        member = sequence.sequence_member
    except Sequence.DoesNotExist as e:        
        last_three = Sequence.objects.all().order_by('-id')[:3]
        start_matrix = [[int(last_three[0].sequence_member), int(last_three[1].sequence_member)],\
        [int(last_three[1].sequence_member), int(last_three[2].sequence_member)]]
        last_index = last_three[0].id
        try:
            member = propagate(start_matrix, n - last_index)
        except RecursionError as re:
            return fib(n)
    return str(member)




def propagate(S, diff):
    I = [[1, 1], [1, 0]]
    if diff == 0:
        return S[0][0]
    else:
        i1 = S[0][0]*I[0][0] + S[0][1]*I[1][0]
        i2 = S[0][0]*I[0][1] + S[0][1]*I[1][1]
        i3 = S[1][0]*I[0][0] + S[1][1]*I[1][0]
        i4 = S[1][0]*I[0][1] + S[1][1]*I[1][1]

        i = Sequence.create(i1)
        i.save()

        S[0][0] = i1
        S[0][1] = i2
        S[1][0] = i3
        S[1][1] = i4

        return propagate(S, diff - 1)
