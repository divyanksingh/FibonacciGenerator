from django.test import TestCase, RequestFactory
from fibonacci.models import Sequence
from fibonacci.utility import fib
from .views import index
import json


class FibonacciTestCase(TestCase):
	def setUp(self):

		Sequence.objects.create(sequence_member = 0)
		Sequence.objects.create(sequence_member = 1)
		Sequence.objects.create(sequence_member = 1)

		self.factory = RequestFactory()


	def test_member_already_in_database(self):

		seq = fib(2)
		self.assertEqual(seq, '1')


	def test_member_added_in_database(self):

		seq = fib(10)
		self.assertEqual(seq, '34')


	def test_api(self):
		body = {"sequence": 100}
		request = self.factory.post('/', data = json.dumps(body), content_type = "application/json")
		response = index(request)
		self.assertEqual(response.status_code, 200)




