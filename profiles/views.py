from rest_framework import generics
from .serializers import RegisterSerializer
from django.contrib.auth.models import User
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Profiles
from .serializers import ProfileSerializer
from rest_framework.permissions import AllowAny

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
class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer
    permission_classes= [AllowAny]








#from rest_framework.generics import ListCreateAPIView
#from .models import Profiles
#from .serializers import ProfileSerializer
#class ProfileListCreateView(ListCreateAPIView):
 #   queryset=Profiles.objects.all()
  #  serializer_class=ProfileSerializer
 
        

