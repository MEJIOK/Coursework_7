from rest_framework import generics
from rest_framework.permissions import AllowAny, IsAdminUser

from users.models import User
from users.paginators import UserPagination
from users.permissions import IsOwner
from users.serializers import UserSerializer


class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    pagination_class = UserPagination
    permission_classes = [IsAdminUser]


class UserUpdate(generics.UpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsOwner]


class UserCreate(generics.CreateAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = [AllowAny]

    def perform_create(self, serializer):
        user = serializer.save(is_active=True)
        user.set_password(user.password)
        user.save()


class UserDelete(generics.DestroyAPIView):
    permission_classes = [IsOwner, IsAdminUser]
    queryset = User.objects.all()
