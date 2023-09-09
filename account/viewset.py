from rest_framework import status, viewsets
from rest_framework.permissions import IsAdminUser, AllowAny, IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate

from .serializers import  UseSerializer, UserLoginSerializer
from .models import User


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    
    queryset = User.objects.all()
    serializer_class = UseSerializer
    permission_classes = [AllowAny]


class UserLoginViewSet(viewsets.ModelViewSet):
    serializer_class = UserLoginSerializer
    permission_classes = [AllowAny]

    def create(self, request):
        serializer = self.serializer_class(data=request.data)
        
        email = request.data.get('email')
        password = request.data.get('password')
        if email is None or password is None:
            return Response({'error': 'Please provide both username and password'},
                            status=status.HTTP_400_BAD_REQUEST)

        user = authenticate(email=email, password=password)
        if not user:
            return Response({'error': 'Invalid Credentials'},
                            status=status.HTTP_404_NOT_FOUND)
        token, created = Token.objects.get_or_create(user=user)
        response = {
            'success': True,
            'statusCode': status.HTTP_200_OK,
            'message': 'User Login Successfully',
            'email': serializer.data['email'],
            'role': serializer.data['role'],
            'token': token.key
        }
        return Response(response)
