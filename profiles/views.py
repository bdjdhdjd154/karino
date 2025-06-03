from rest_framework import generics
from .serializers import RegisterSerializer
from django.contrib.auth.models import User
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Profiles
from .serializers import ProfileSerializer
from rest_framework.permissions import AllowAny
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.models import Token
from rest_framework import status
from rest_framework.decorators import api_view
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view, permission_classes
from django.contrib.auth import authenticate


class ProfileListCreateView(APIView):
    def get(self, request):
        profiles = Profiles.objects.all()
        serializer = ProfileSerializer(profiles, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ProfileSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
@permission_classes([AllowAny])
def register_view(request):
    serializer = RegisterSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["POST"])
def login_api_view(request):
    username = request.data.get("username")
    password = request.data.get("password")

    user = authenticate(username=username, password=password)

    if user is not None:
        token, created = Token.objects.get_or_create(user=user)
        return Response({"token": token.key}, status=200)
    return Response({"detail": "نام کاربری یا رمز عبور اشتباه است"}, status=status.HTTP_401_UNAUTHORIZED)


class MyProfileView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        try:
            profile = Profiles.objects.get(user=request.user)
        except Profiles.DoesNotExist:    
            return Response({'error': 'Profile not found'}, status=404)

        serializer = ProfileSerializer(profile)
        return Response(serializer.data)
class ProfileDetailView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        try:
            profile = Profiles.objects.get(user=request.user)
            serializer = ProfileSerializer(profile)
            return Response(serializer.data)
        except Profiles.DoesNotExist:
            return Response({"error": "Profile not found"}, status=404)        
class ProfileUpdateView(generics.RetrieveUpdateAPIView):
    queryset = Profiles.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        return self.request.user.profiles

class LogoutView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        try:
            request.user.auth_token.delete() # حذف توکن
            return Response({"detail": "Logout successful."}, status=status.HTTP_200_OK)
        except:
            return Response({"error": "Something went wrong."}, status=status.HTTP_400_BAD_REQUEST)
            






#from rest_framework.generics import ListCreateAPIView
#from .models import Profiles
#from .serializers import ProfileSerializer
#class ProfileListCreateView(ListCreateAPIView):
 #   queryset=Profiles.objects.all()
  #  serializer_class=ProfileSerializer
 
        

