from django.db import models

class Sequence(models.Model):
    sequence_member = models.TextField()

    @classmethod
    def create(cls, member):
        new_member = cls(sequence_member=member)
        return new_member