from rest_framework import generics, permissions
from django.contrib.auth.models import User
from .models import Company
from .serializers import CompanyRegisterSerializer, CompanyProfileSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.models import Token
from rest_framework import status

class LogoutView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        try:
            request.user.auth_token.delete() # حذف توکن
            return Response({"detail": "Logout successful."}, status=status.HTTP_200_OK)
        except:
            return Response({"error": "Something went wrong."}, status=status.HTTP_400_BAD_REQUEST)

class CompanyRegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = CompanyRegisterSerializer

class MyCompanyProfileView(generics.RetrieveAPIView):
    serializer_class = CompanyProfileSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        return Company.objects.get(user=self.request.user)


class LogoutView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        try:
            request.user.auth_token.delete() 
            return Response({"detail": "Logout successful."}, status=status.HTTP_200_OK)
        except:
            return Response({"error": "Something went wrong."}, status=status.HTTP_400_BAD_REQUEST)
# Create your views here.
