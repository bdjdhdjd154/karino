"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from profiles.views import CustomAuthToken
from django.contrib import admin
from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenRefreshView
from django.conf import settings
from django.conf.urls.static import static
from main import views


urlpatterns = [
    
    path('admin/', admin.site.urls),
    path('api/', include('profiles.urls')),
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),
    path('api/', include('profiles.urls')),
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),
    path('admin',admin.site.urls),
    path('api/login/', obtain_auth_token, name='api_token_auth'),
    path('login/',CustomAuthToken.as_view(), name='login'),
    path('api/profile/', include('profiles.urls')),
    path('api/', include('profiles.urls')),
    path('api/register', TokenRefreshView.as_view(), name='register'),
    path('api/login', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/', include('company.urls')),
    path('api/company/', include('company.urls')),
    path('api/profiles/', include('profiles.urls')),
    path('api/company/', include('company.urls')), 
   ## path('', include('main.urls')),

]
##if settings.DEBUG:
    ##urlpatterns+= static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)