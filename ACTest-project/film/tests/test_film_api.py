from django.contrib.auth import get_user_model
from django.urls import reverse
from django.test import TestCase

from rest_framework import status
from rest_framework.test import APIClient

from core.models import Film, Tag, Genre

from film.serializers import FilmSerializer, FilmDetailSerializer

FILMS_URL = reverse('film:film-list')


# /api/film/films/1
def detail_url(film_id):
	"""Return film detail URL"""
	return reverse('film:film-detail', args=[film_id])


def sample_tag(user, name='Netflix'):
	"""Create and return a sample tag"""
	return Tag.objects.create(user=user, name=name)


def sample_genre(user, name='Comedy'):
	"""Create and return a sample genre"""
	return Genre.objects.create(user=user, name=name)


def sample_film(user, **params):
	"""Create and return a sample film"""
	defaults = {
		'title': 'Sample film',
		'time_minutes': 90,
		'year': 2018,
	}
	# If added params to sample_film it will override or be added to defaults
	defaults.update(params)

	return Film.objects.create(user=user, **defaults)


class PublicFilmApiTest(TestCase):
	"""Test unauthenticated film API access"""

	def setUp(self):
		self.client = APIClient()

	def test_auth_required(self):
		"""Test that authentication is required"""
		res = self.client.get(FILMS_URL)

		# Test that it returned unauthorized
		self.assertEqual(res.status_code, status.HTTP_401_UNAUTHORIZED)


class PrivateFilmApiTests(TestCase):
	"""Test authenticated film API access"""

	def setUp(self):
		self.client = APIClient()
		self.user = get_user_model().objects.create_user(
			'test@gmail.com',
			'testPassword123',
		)
		self.client.force_authenticate(self.user)

	def test_retrieve_films_list(self):
		"""Test retrieving a list of films"""

		sample_film(user=self.user)
		sample_film(user=self.user)

		res = self.client.get(FILMS_URL)

		films = Film.objects.all().order_by('-id')
		serializer = FilmSerializer(films, many=True)

		#for k in res.data:
			#print(k)

		#for k in serializer.data:
			#print(k)

		# Compare the result to the serialized films
		self.assertEqual(res.status_code, status.HTTP_200_OK)
		self.assertEqual(res.data, serializer.data)

	def test_films_limited_to_user(self):
		"""Test retrieving films for user"""

		user2 = get_user_model().objects.create_user(
			'otherUser@gmail.com',
			'anotherTestPassword'
		)
		# Create film object with this new user
		sample_film(user=user2)
		# Create another film assigned to the authenticated user
		sample_film(user=self.user)

		res = self.client.get(FILMS_URL)

		# Filter films by the authenticated user
		films = Film.objects.filter(user=self.user)
		serializer = FilmSerializer(films, many=True)

		self.assertEqual(res.status_code, status.HTTP_200_OK)
		# Expected just 1 created film for the user
		self.assertEqual(len(res.data), 1)
		self.assertEqual(res.data, serializer.data)

	def test_view_film_detail(self):
		"""Test viewing a film detail"""
		film = sample_film(user=self.user)
		film.tags.add(sample_tag(user=self.user))
		film.genres.add(sample_genre(user=self.user))

		# Generate url
		url = detail_url(film.id)
		res = self.client.get(url)

		serializer = FilmDetailSerializer(film)
		self.assertEqual(res.data, serializer.data)