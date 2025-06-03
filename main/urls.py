from django.urls import path
from main.views import home
from . import views
from .views import karino_view
urlpatterns=[
    path('', home, name='home'),
    path('register/', views.myregister_view, name='register'),
    path('login/', views.mylogin_view, name='login' ),
    path('karino/', karino_view, name='karino')
]