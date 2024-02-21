from django.urls import path

from account.views import (
    UserRegistrationView, UserLoginview, UserProfileView, UserChangePasswordView,
    UserDeleteView
)


urlpatterns = [
    path('', UserProfileView.as_view(), name='profile'),
    path('<int:pk>/', UserDeleteView.as_view(), name='profile'),
    path('<int:pk>/', UserChangePasswordView.as_view(), name='change-password'),
    path('register/', UserRegistrationView.as_view(), name='register'),
    path('login/', UserLoginview.as_view(), name='login'),
    path('changepassword/', UserChangePasswordView.as_view(), name='change-password'),

]
