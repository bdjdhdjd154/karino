from django.urls import path
from main import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView
)
urlpatterns=[
    path('', views.main, name='main'),
    path('api/')
]