from rest_framework import generics, response, status
from rest_framework.permissions import IsAuthenticated
from . import serializers
from .models import User
from .permissions import IsAdminOrReadOnly


class UserRegister(generics.CreateAPIView):
    """
    Register a new `User`.
    """

    serializer_class = serializers.RegistrationSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            user = serializer.save()
            message = "Your account has been created."
            return response.Response(
                data={"data": message},
                status=status.HTTP_201_CREATED,
            )


class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = serializers.UserSerializer


class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = serializers.ProfileSerializer
    permission_classes = (IsAuthenticated, IsAdminOrReadOnly)

class ProfileDetail(generics.RetrieveUpdateDestroyAPIView):
    model = User
    serializer_class = serializers.ProfileSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        return self.request.user
