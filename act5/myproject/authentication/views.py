from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import RegisterSerializer
from rest_framework import generics

class ProtectedView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        return Response({'message': 'Welcome, authenticated user!'})
    
class RegisterView(generics.CreateAPIView):
    serializer_class = RegisterSerializer
