from django.urls import path

from user import views

app_name = 'user'

urlpatterns = [
	path('create/', views.CreateUserView.as_view(), name='create'), # matches the name in test_user_api.py file
	path('token/', views.CreateTokenView.as_view(), name='token'), # matches the name in test_user_api.py file
	path('me/', views.ManageUserView.as_view(), name='me'), # matches the name in test_user_api.py file
]