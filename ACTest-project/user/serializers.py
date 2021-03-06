from django.contrib.auth import get_user_model, authenticate
from django.utils.translation import gettext_lazy as _

from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
	"""Serializer for the users object"""

	class Meta:
		model = get_user_model()
		# Fields that we're going to accept when creating users:
		fields = ('email', 'password', 'name')
		extra_kwargs = {'password': {'write_only': True, 'min_length': 5}}

	def create(self, validated_data):
		"""Create a new user with encrypted password and return it"""
		# 'validated_data' will contains all data that was passed into serializer (JSON made in HTTP POST)
		# We can then use that to create our user
		return get_user_model().objects.create_user(**validated_data)
	
	# instance = model instance that is linked to ModelSerializer
	# validated_data = fields ready to update
	def update(self, instance, validated_data):
		"""Update a user, setting the password correctly and return it"""

		# Remove the password from the validated data
		password = validated_data.pop('password', None)

		user = super().update(instance, validated_data)

		# If the user provides a password
		if password:
			user.set_password(password)
			user.save()

		return user
		

class AuthTokenSerializer(serializers.Serializer):
	"""Serializer for the user authentication object"""
	email = serializers.CharField()
	password = serializers.CharField(
		style={'input_type': 'password'},
		trim_whitespace=False
	)

	def validate(self, attrs):
		"""Validate and authenticate the user"""
		email = attrs.get('email')
		password = attrs.get('password')

		user = authenticate(
			request = self.context.get('request'),
			username=email,
			password=password
		)
		if not user:
			msg = _('Unable to authenticate with provided credentials')
			raise serializers.ValidationError(msg, code='authentication')

		attrs['user'] = user
		return attrs

