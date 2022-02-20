from unittest.mock import patch

from django.core.management import call_command
from django.db.utils import OperationalError
from django.test import TestCase

class CommandTest(TestCase):

	def test_wait_for_db_ready(self):
		"""Test waiting for db when db is available"""
		# overwrite the behaviour of the connection handler to not trow an exception
		with patch('django.db.utils.ConnectionHandler.__getitem__') as gi:
			# I'm gonna mock the behaviour of this __getitem__ to returns True
			gi.return_value = True
			call_command('wait_for_db')
			# check that __getitem__ was called once
			self.assertEqual(gi.call_count, 1)

	# mocking the delay of time.sleep in our tests
	@patch('time.sleep', return_value=True)
	def test_wait_for_db(self, ts): # pass the time.sleep as parameter
		"""Test waiting for db"""
		with patch('django.db.utils.ConnectionHandler.__getitem__') as gi:
			# raise OperationalError 5 times and in the 6th it will be successful
			gi.side_effect = [OperationalError] *5 + [True]
			call_command('wait_for_db')
			# check that __getitem__ was called 6 times
			self.assertEqual(gi.call_count, 6)