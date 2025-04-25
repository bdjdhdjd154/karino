from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from .serializers import ProfileSerializer

@api_view(['POST'])
def register_user(request):
    """
    ثبت‌نام کاربر جدید
    """
    if request.method == 'POST':
        # ثبت‌نام و ایجاد پروفایل جدید
        user_serializer = ProfileSerializer(data=request.data)
        if user_serializer.is_valid():
            user_serializer.save() # ذخیره اطلاعات کاربر
            user = User.objects.create_user(
                username=request.data['username'],
                password=request.data['password']
            )
            token = Token.objects.create(user=user) # ایجاد توکن
            return Response({
                'user': user_serializer.data,
                'token': token.key
            }, status=status.HTTP_201_CREATED)
        return Response(user_serializer.errors, status=status.HTTP_400_BAD_REQUEST)









#from rest_framework.generics import ListCreateAPIView
#from .models import Profiles
#from .serializers import ProfileSerializer
#class ProfileListCreateView(ListCreateAPIView):
 #   queryset=Profiles.objects.all()
  #  serializer_class=ProfileSerializer
 
        

