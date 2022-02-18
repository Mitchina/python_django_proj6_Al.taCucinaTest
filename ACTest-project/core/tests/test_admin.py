from django.test import TestCase, Client
from django.contrib.auth import get_user_model
from django.urls import reverse

class AdminSiteTests(TestCase):

	def setUp(self):
		self.client = Client()
		self.admin_user = get_user_model().objects.create_superuser(
			email='admin@gmail.com',
			password='adminPassword123'
		)

		# The admin is logged into the client
		self.client.force_login(self.admin_user)
		# Spare user that we can use for testing listing and things like that
		self.user = get_user_model().objects.create_user(
			email = 'test@gmail.com',
			password = 'password123',
			name = 'Test user full name'
		)

	def test_users_listed(self):
		"""Test that users are listed on user page"""
		url = reverse('admin:core_user_changelist')
		# use our test client to perform a HTTP GET on the URL that we have found:
		res = self.client.get(url)

		self.assertContains(res, self.user.name)
		self.assertContains(res, self.user.email)

	def test_user_change_page(self):
		"""Test that the user edit page works"""
		# /admin/core/user/userId
		url = reverse('admin:core_user_change', args=[self.user.id])
		
		# http GET test in the url
		res = self.client.get(url)
		
		# test if the status code for the response is http 200, means the page works
		self.assertEquals(res.status_code, 200)

	def test_create_user_page(self):
		"""Test that the create user page works"""
		url = reverse('admin:core_user_add')
		res = self.client.get(url)

		self.assertEquals(res.status_code, 200)
