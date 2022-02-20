from rest_framework import generics
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings

from user.serializers import UserSerializer, AuthTokenSerializer

class CreateUserView(generics.CreateAPIView):
	"""Create a new user in the system"""
	# Points to the serializer class that we want to use to create objects in the database
	serializer_class = UserSerializer

class CreateTokenView(ObtainAuthToken):
	"""Create a new auth token for user"""
	serializer_class = AuthTokenSerializer
	# view endpoit in the browser, it should return the token
	renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES