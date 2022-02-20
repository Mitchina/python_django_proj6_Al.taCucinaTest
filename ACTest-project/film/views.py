from rest_framework import viewsets, mixins
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from core.models import Tag

from film import serializers


class TagViewSet(viewsets.GenericViewSet, mixins.ListModelMixin):
	"""Manage tags in the database"""
	authentication_classes = (TokenAuthentication, )
	permission_classes = (IsAuthenticated, )
	# Provide the queryset that you wanna return
	queryset = Tag.objects.all()
	serializer_class = serializers.TagSerializer

	def get_queryset(self):
		"""Return objects for the current authenticated user only"""
		# Limiting objects to the authenticated user
		return self.queryset.filter(user=self.request.user).order_by('-name')
