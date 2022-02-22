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

	def test_create_basic_film(self):
		"""Test creating a film"""
		payload = {
			'title': 'The Hunger Games',
			'time_minutes': 142,
			'year': 2012,
		}
		res = self.client.post(FILMS_URL, payload)

		# 201 for created objs
		self.assertEqual(res.status_code, status.HTTP_201_CREATED)
		# Retrieve the created film from our model
		film = Film.objects.get(id=res.data['id'])

		for key in payload.keys():
			# Assert that the field in payload same as created film
			self.assertEqual(payload[key], getattr(film, key))

	def test_create_film_with_tags(self):
		"""Test creating a film with tags"""
		tag1 = sample_tag(user=self.user, name='Netflix')
		tag2 = sample_tag(user=self.user, name='Amazon Prime Video')
		payload = {
			'title': 'Interstellar',
			'time_minutes': 169,
			'year': 2014,
			'tags': [tag1.id, tag2.id],
		}
		res = self.client.post(FILMS_URL, payload)

		self.assertEqual(res.status_code, status.HTTP_201_CREATED)
		film = Film.objects.get(id=res.data['id'])
		tags = film.tags.all()

		self.assertEqual(tags.count(), 2)
		self.assertIn(tag1, tags)
		self.assertIn(tag2, tags)

	def test_create_film_with_genres(self):
		"""Test creating a film with genres"""
		genre1 = sample_genre(user=self.user, name='Fantasy')
		genre2 = sample_genre(user=self.user, name='Adventure')
		payload = {
			'title': 'Fantastic Beasts: The Crimes of Grindelwald',
			'time_minutes': 134,
			'year': 2018,
			'genres': [genre1.id, genre2.id],
		}
		res = self.client.post(FILMS_URL, payload)

		self.assertEqual(res.status_code, status.HTTP_201_CREATED)
		film = Film.objects.get(id=res.data['id'])
		genres = film.genres.all()

		self.assertEqual(genres.count(), 2)
		self.assertIn(genre1, genres)
		self.assertIn(genre2, genres)

	def test_partial_update_film(self):
		"""Test updating a film with a patch method"""
		film = sample_film(user=self.user)
		film.tags.add(sample_tag(user=self.user))
		new_tag = sample_tag(user=self.user, name='Disney+')

		# Expected name and tags replaced with 'Replace Title' and new_tag 
		payload = {
			'title': 'Replace Sample Title',
			'tags': [new_tag.id],
		}		

		# Generate url
		url = detail_url(film.id)
		self.client.patch(url, payload)

		film.refresh_from_db()
		self.assertEqual(film.title, payload['title'])

		tags = film.tags.all()
		self.assertEqual(len(tags), 1)
		self.assertIn(new_tag, tags)

	def test_full_update_film(self):
		"""Test updating a film with a put method"""
		film = sample_film(user=self.user)
		film.tags.add(sample_tag(user=self.user))
		payload = {
			'title': 'Replace Sample Title',
			'time_minutes': 112,
			'year': 2015,
		}
		url = detail_url(film.id)
		self.client.put(url, payload)

		film.refresh_from_db()
		self.assertEqual(film.title, payload['title'])
		self.assertEqual(film.time_minutes, payload['time_minutes'])
		self.assertEqual(film.year, payload['year'])

		# Expected that film has no more tags assigned
		tags = film.tags.all()
		self.assertEqual(len(tags), 0)

	def test_filter_films_by_tags(self):
		"""Test returning films with specific tags"""
		film1 = sample_film(user=self.user, title='The Revenant')
		film2 = sample_film(user=self.user, title='Fantastic Four')
		tag1 = sample_tag(user=self.user, name='Netflix')
		tag2 = sample_tag(user=self.user, name='Disney+')
		film1.tags.add(tag1)
		film2.tags.add(tag2)
		film3 = sample_film(user=self.user, title='Avengers: Age of Ultron')

		res = self.client.get(
			FILMS_URL,
			# Dict of values that you wish to add as get parameters
			{'tags': f'{tag1.id}, {tag2.id}'}
		)

		# Serialize films and check if they exist in the res returned
		serializer1 = FilmSerializer(film1)
		self.assertIn(serializer1.data, res.data)
		serializer2 = FilmSerializer(film2)
		self.assertIn(serializer2.data, res.data)
		serializer3 = FilmSerializer(film3)
		self.assertNotIn(serializer3.data, res.data)

	def test_filter_films_by_genres(self):
		"""Test returning films with specific genres"""
		film1 = sample_film(user=self.user, title='The Revenant')
		film2 = sample_film(user=self.user, title='Fantastic Four')
		genre1 = sample_genre(user=self.user, name='Western')
		genre2 = sample_genre(user=self.user, name='Action')
		film1.genres.add(genre1)
		film2.genres.add(genre2)
		film3 = sample_film(user=self.user, title='Avengers: Age of Ultron')

		res = self.client.get(
			FILMS_URL,
			# Dict of values that you wish to add as get parameters
			{'genres': f'{genre1.id}, {genre2.id}'}
		)

		# Serialize films and check if they exist in the res returned
		serializer1 = FilmSerializer(film1)
		self.assertIn(serializer1.data, res.data)
		serializer2 = FilmSerializer(film2)
		self.assertIn(serializer2.data, res.data)
		serializer3 = FilmSerializer(film3)
		self.assertNotIn(serializer3.data, res.data)

	def test_filter_films_by_have_seen(self):
		"""Test returning films that have been seen"""
		film1 = sample_film(user=self.user, title='The Revenant', have_seen=True)
		film2 = sample_film(user=self.user, title='Fantastic Four', have_seen=True)
		film3 = sample_film(user=self.user, title='Avengers: Age of Ultron', have_seen=False)

		res = self.client.get(FILMS_URL, {'have_seen': 'True'})

		# Serialize films and check if they exist in the res returned
		serializer1 = FilmSerializer(film1)
		self.assertIn(serializer1.data, res.data)
		serializer2 = FilmSerializer(film2)
		self.assertIn(serializer2.data, res.data)
		serializer3 = FilmSerializer(film3)
		self.assertNotIn(serializer3.data, res.data)

	def test_filter_films_by_have_not_seen(self):
		"""Test returning films that have not been seen"""
		film1 = sample_film(user=self.user, title='The Revenant', have_seen=True)
		film2 = sample_film(user=self.user, title='Fantastic Four', have_seen=False)
		film3 = sample_film(user=self.user, title='Avengers: Age of Ultron', have_seen=False)

		res = self.client.get(FILMS_URL, {'have_seen': 'False'})

		# Serialize films and check if they exist in the res returned
		serializer1 = FilmSerializer(film1)
		self.assertNotIn(serializer1.data, res.data)
		serializer2 = FilmSerializer(film2)
		self.assertIn(serializer2.data, res.data)
		serializer3 = FilmSerializer(film3)
		self.assertIn(serializer3.data, res.data)