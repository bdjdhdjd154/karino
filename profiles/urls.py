from django.urls import path
from .views import ProfileListCreateView
from .views import RegisterView


urlpatterns = [
    path('profiles/', ProfileListCreateView.as_view(), name='profile-list'),
    path('register/', RegisterView.as_view(), name='register'),

]