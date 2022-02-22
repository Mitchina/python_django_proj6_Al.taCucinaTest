from rest_framework import viewsets, mixins
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from core.models import Tag, Genre, Film

from film import serializers

class BaseFilmAttrViewSet(viewsets.GenericViewSet, 
				mixins.ListModelMixin,
				mixins.CreateModelMixin):
	"""Base viewset for user owned film attributes"""
	"""Manage attributes in the database"""
	authentication_classes = (TokenAuthentication, )
	permission_classes = (IsAuthenticated, )

	def get_queryset(self):
		"""Return objects for the current authenticated user only"""
		# Limiting objects to the authenticated user
		return self.queryset.filter(user=self.request.user).order_by('-name')

	# Perfom modifications to our create proccess
	def perform_create(self, serializer):
		"""Create a new object"""
		serializer.save(user=self.request.user)


class TagViewSet(BaseFilmAttrViewSet):
	# Provide the queryset that you wanna return
	queryset = Tag.objects.all()
	serializer_class = serializers.TagSerializer


class GenreViewSet(BaseFilmAttrViewSet):
	queryset = Genre.objects.all()
	serializer_class = serializers.GenreSerializer


class FilmViewSet(viewsets.ModelViewSet):
	"""Manage films in the database"""

	queryset = Film.objects.all()	
	serializer_class = serializers.FilmSerializer

	authentication_classes = (TokenAuthentication, )
	permission_classes = (IsAuthenticated, )

	def get_queryset(self):
		"""Retrieve the films for the authenticated user"""
		return self.queryset.filter(user=self.request.user)

	def get_serializer_class(self):
		"""Return appropriate serializer class"""
		if self.action == 'retrieve':
			# When calling the retrieve action, use FilmDetailSerializer
			return serializers.FilmDetailSerializer

		return self.serializer_class

	# Assign user of the film to the current authenticated user
	def perform_create(self, serializer):
		"""Create a new film"""
		serializer.save(user=self.request.user)



