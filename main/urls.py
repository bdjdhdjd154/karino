from django.urls import path
from main.views import home
from . import views
from .views import karino_view
urlpatterns=[
    path('', home, name='home'),
    path('register/', views.myregister_view, name='register'),
    path('login/', views.mylogin_view, name='login' ),
    path('karino/', karino_view, name='karino'),
    path('intership/', views.intership_view, name='intership'),
    path('employer/', views.employer_view, name='employer' ),
    path('forgot-password/', views.reg2_view, name='reg2')




]