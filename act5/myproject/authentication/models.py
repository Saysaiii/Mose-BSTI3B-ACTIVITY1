from django.contrib.auth.models import User
from rest_framework import generics, serializers
from rest_framework_simplejwt.views import TokenObtainPairView

class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email', 'password')

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)

class RegisterView(generics.CreateAPIView):
    serializer_class = RegisterSerializer

class LoginView(TokenObtainPairView):
    pass