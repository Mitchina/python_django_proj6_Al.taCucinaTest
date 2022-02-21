from rest_framework import serializers

from core.models import Tag, Genre


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
