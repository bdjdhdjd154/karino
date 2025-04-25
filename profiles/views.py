from rest_framework.generics import ListCreateAPIView
from .models import Profiles
from .serializers import ProfileSerializer

class ProfileListCreateView(ListCreateAPIView):
        queryset = Profiles.objects.all()
        serializer_class = ProfileSerializer
        

