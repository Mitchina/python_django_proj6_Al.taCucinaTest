from django.contrib.auth import get_user_model
from django.urls import reverse
from django.test import TestCase

from rest_framework import status
from rest_framework.test import APIClient

from core.models import Tag

from film.serializers import TagSerializer

TAGS_URL = reverse('film:tag-list')


class PublicTagsApiTests(TestCase):
	"""Test the publicly available tags API"""

	def setUp(self):
		self.client = APIClient()

	def test_login_required(self):
		"""Test that login is required for retrieving tags"""
		res = self.client.get(TAGS_URL)

		self.assertEqual(res.status_code, status.HTTP_401_UNAUTHORIZED)


class PrivateTagsApiTests(TestCase):
	"""Test the authorized user tags API"""

	def setUp(self):
		self.user = get_user_model().objects.create_user(
			'test@gmail.com',
			'password123'
		)
		self.client = APIClient()
		self.client.force_authenticate(self.user)

	def test_retrieve_tags(self):
		"""Test retrieving tags"""
		Tag.objects.create(user=self.user, name='Netflix')
		Tag.objects.create(user=self.user, name='Prime')

		# Return tags
		res = self.client.get(TAGS_URL)
		# Serialize the list of objects
		tags = Tag.objects.all().order_by('-name')
		serializer = TagSerializer(tags, many=True)
		self.assertEqual(res.status_code, status.HTTP_200_OK)
		self.assertEqual(res.data, serializer.data)

	def test_tags_limited_to_user(self):
		"""Test that tags returned are for the authenticated user"""
		user2 = get_user_model().objects.create_user(
			'testOtherUser@gmail.com',
			'otherUserPassword123'
		)
		Tag.objects.create(user=user2, name='Disney Plus')
		tag = Tag.objects.create(user=self.user, name='HBO Max')

		res = self.client.get(TAGS_URL)

		self.assertEqual(res.status_code, status.HTTP_200_OK)
		# Just one tag is expected to return to the authenticated user
		self.assertEqual(len(res.data), 1)
		# Assert tag name returned is that created for the user
		self.assertEqual(res.data[0]['name'], tag.name)

	def test_create_tag_successful(self):
		"""Test creating a new tag"""
		payload = {'name': 'Test tag'}
		self.client.post(TAGS_URL, payload)

		# Verify that the tag exists
		exists = Tag.objects.filter(
			user = self.user,
			name = payload['name']
		).exists()
		self.assertTrue(exists)

	def test_create_tag_invalid(self):
		"""Test creating a new tag with invalid payload"""
		payload = {'name': ''}
		res = self.client.post(TAGS_URL, payload)

		self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)
