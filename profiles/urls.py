from django.urls import path
from .views import ProfileListCreateView
from .views import RegisterView
from .views import MyProfileView
from .views import ProfileDetailView
from .views import ProfileUpdateView



urlpatterns = [
    path('profiles/', ProfileListCreateView.as_view(), name='profile-list'),
    path('register/', RegisterView.as_view(), name='register'),
    path('me/', MyProfileView.as_view(), name='my-profile'),
    path('profile/', ProfileDetailView.as_view(), name='profile-detail'),
    path('profile/', ProfileUpdateView.as_view(), name='profile-update'),

]