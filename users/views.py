from rest_framework.generics import CreateAPIView
from rest_framework.permissions import AllowAny

from .serializers import UserRegisterSerializer


class UserRegister(CreateAPIView):
    serializer_class = UserRegisterSerializer
    permission_classes = [AllowAny]
