from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework import generics, status
from rest_framework.permissions import AllowAny
from .models import User
from .serializers import UserSerializer


class CreateUserView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (AllowAny,)

    def create(self, request: Request, *args, **kwargs):
        try:
            response = super().create(request, *args, **kwargs)
            # Генерация токена после успешного создания пользователя
            refresh = RefreshToken.for_user(self.user)
            response.data['token'] = {
                'refresh': str(refresh),
                'access': str(refresh.access_token),
            }
            return response
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)