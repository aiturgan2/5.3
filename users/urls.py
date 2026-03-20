from django.urls import path
from .views import RegisterAPIVIew, ProfileAPIVIew

urlpatterns = [
    path("register", RegisterAPIVIew.as_view(), name='register'),
    path("profile", ProfileAPIVIew.as_view(), name='profile'),
]
