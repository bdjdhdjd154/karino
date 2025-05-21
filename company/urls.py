from django.urls import path ,include
from .views import CompanyRegisterView, MyCompanyProfileView
from .views import LogoutView


urlpatterns = [
    path('register/', CompanyRegisterView.as_view(), name='company-register'),
    path('me/', MyCompanyProfileView.as_view(), name='my-company-profile'),
    path('logout/', LogoutView.as_view(), name='logout'),
]