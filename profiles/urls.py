from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register_view, name='register'),  # 🔹 توجه: class-based
    path('me/', views.MyProfileView.as_view(), name='my-profile'),
    path('profile/', views.ProfileDetailView.as_view(), name='profile-detail'),
    path('profile/update/', views.ProfileUpdateView.as_view(), name='profile-update'),  # جداش کن
    path('logout/', views.LogoutView.as_view(), name='logout'),
]
