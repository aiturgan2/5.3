from rest_framework.generics import CreateAPIView, RetrieveAPIView
from rest_framework.permissions import IsAuthenticated, AllowAny

from .models import User
from .serializers import UserProfileSerializer, UserRegisterSerializer

class RegisterAPIVIew(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserRegisterSerializer
    permission_classes = [AllowAny]

class ProfileAPIVIew(RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserProfileSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        return self.request.user
