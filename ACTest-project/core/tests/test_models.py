from django.test import TestCase
from django.contrib.auth import get_user_model

from core import models


# Helper function to create users in the tests
def sample_user(email='test@gmail.com', password = 'Testpassword123'):
	"""Create a sample user"""
	return get_user_model().objects.create_user(email, password)


class ModelTests(TestCase):
	"""Testing creating a new user with an email is successful"""

	def test_create_user_with_email_successful(self):
		# creating a test email
		email = 'test@gmail.com'
		password = 'Testpassword123'
		user = get_user_model().objects.create_user(
			email=email, 
			password=password
		)

		self.assertEqual(user.email, email)
		self.assertTrue(user.check_password(password))

	def test_new_user_email_normalized(self):
		"""Test the email for a new user is normalized"""
		email = 'test@GMAIL.COM'
		user = get_user_model().objects.create_user(
			email, 'randomPasswordTest123'
		)

		self.assertEqual(user.email, email.lower())

	def test_new_user_invalid_email(self):
		"""Test creating user with no email raises error"""
		with self.assertRaises(ValueError):
			get_user_model().objects.create_user(None, 'randomPasswordTest123')

	def test_create_new_superuser(self):
		"""Test creating a new superuser"""
		user = get_user_model().objects.create_superuser(
			'randomEmailTest@gmail.com', 'randomPasswordTest123'
		)

		self.assertTrue(user.is_superuser)
		self.assertTrue(user.is_staff)
	
	def test_tag_str(self):
		"""Test the tag string representation"""
		tag = models.Tag.objects.create(
			user=sample_user(),
			name='Netflix'
		)

		# Verify creation of a model called tag
		self.assertEqual(str(tag), tag.name)

	def test_genre_str(self):
		"""Test the genre string representation"""
		genre = models.Genre.objects.create(
			user=sample_user(),
			name='Comedy',
		)

		self.assertEqual(str(genre), genre.name)

	def test_film_str(self):
		"""Test the film string representation"""
		film = models.Film.objects.create(
			# required fields
			user=sample_user(),
			title='Jumanji the next level',
			time_minutes=123,
			year=2019,
		)

		self.assertEqual(str(film), film.title)