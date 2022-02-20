from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse

from rest_framework.test import APIClient
from rest_framework import status

CREATE_USER_URL = reverse('user:create') # matches the name in urls.py file
TOKEN_URL = reverse('user:token') # matches the name in urls.py file

def create_user(**params):
	return get_user_model().objects.create_user(**params)


class PublicUserApiTests(TestCase):
	"""Test the users API (public)"""

	def setUp(self):
		self.cliente = APIClient()

	def test_create_valid_user_success(self):
		"""Test creating user with valid payload is successful"""
		payload = {
			'email': 'test@gmail.com',
			'password': 'testPassword',
			'name': 'Test Name',
		}
		# Make request and store in response
		res = self.cliente.post(CREATE_USER_URL, payload)

		self.assertEqual(res.status_code, status.HTTP_201_CREATED)

		# Test if the object is actually created
		user = get_user_model().objects.get(**res.data)
		# Assert that the password is true
		self.assertTrue(user.check_password(payload['password']))
		# Assert that the password is not being returned as part of that object (data)
		self.assertNotIn('password', res.data)


	def test_user_exists(self):
		"""Test creating a user that already exists fails"""
		payload = {
			'email': 'test@gmail.com',
			'password': 'testPassword',
			'name': 'Test Name',
		}
		create_user(**payload)

		res = self.cliente.post(CREATE_USER_URL, payload)

		self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)


	def test_password_too_short(self):
		"""Test that the password must be more than 5 characters"""
		payload = {
			'email': 'test@gmail.com',
			'password': 'pw',
			'name': 'Test Name',
		}

		res = self.cliente.post(CREATE_USER_URL, payload)

		self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)
		# Filter for any user with this email address
		user_exists = get_user_model().objects.filter(
			email=payload['email']
		).exists()
		# If the user exists it will return true otherwise false
		self.assertFalse(user_exists)


	def test_create_token_for_user(self):
		'''Test that a token is created for the user'''
		payload = {
			'email': 'test@gmail.com',
			'password': 'testPassword',
		}
		create_user(**payload)

		res = self.cliente.post(TOKEN_URL, payload)

		# We should get a HTTP 200 res and it should contain a token in the data res
		self.assertIn('token', res.data)
		self.assertEqual(res.status_code, status.HTTP_200_OK)


	def test_create_token_invalid_credentials(self):
		"""Test that token is not created if invalid credentials are given"""
		create_user(email='test@gmail.com', password='testPassword')
		payload = {
			'email': 'test@gmail.com',
			'password': 'wrongPass',
		}

		res = self.cliente.post(TOKEN_URL, payload)

		# We expect token doesn't exist in response
		self.assertNotIn('token', res.data)
		self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)


	def test_create_token_no_user(self):
		"""Test that token is not created if user doesn't exist"""
		payload = {
			'email': 'test@gmail.com',
			'password': 'testPassword',
		}
		# Make request and store in response
		res = self.cliente.post(TOKEN_URL, payload)

		# We expect to be no token and a HTTP 400
		self.assertNotIn('token', res.data)
		self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)


	def test_create_token_missing_field(self):
		"""Test that email and password are required"""
		res = self.cliente.post(TOKEN_URL, {'email': 'one', 'password': ''})

		self.assertNotIn('token', res.data)
		self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)
