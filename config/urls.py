from django.contrib import admin
from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('profiles.urls')),  # فقط یکبار کافیه
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),  # Token auth
  
    path('', include('main.urls')),  # فرانت‌اند و صفحات HTML
]


##if settings.DEBUG:
    ##urlpatterns+= static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)