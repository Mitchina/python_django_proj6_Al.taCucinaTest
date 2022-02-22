from rest_framework import serializers

from core.models import Tag, Genre, Film


class TagSerializer(serializers.ModelSerializer):
	"""Serializer for tag objects"""

	class Meta:
		model = Tag
		fields = ('id', 'name')
		read_only_fields = ('id',)


class GenreSerializer(serializers.ModelSerializer):
	"""Serializer for genre objects"""

	class Meta:
		model = Genre
		fields = ('id', 'name')
		read_only_fields = ('id',)


class FilmSerializer(serializers.ModelSerializer):
	"""Serializer for film objects"""
	tags = serializers.PrimaryKeyRelatedField(
		many=True,
		# List the tags with their id
		queryset=Tag.objects.all()
	)
	genres = serializers.PrimaryKeyRelatedField(
		many=True,
		# List the genres with their id
		queryset=Genre.objects.all()
	)

	class Meta:
		model = Film
		fields = (
			'id', 'title', 'time_minutes', 'year', 
			'have_seen', 'link', 'tags', 'genres',
		)
		read_only_fields = ('id',)
