from django.urls import path
from .views import ProtectedView, RegisterView
from rest_framework_simplejwt.views import TokenObtainPairView


urlpatterns = [
    path('protected/', ProtectedView.as_view(), name='protected'),
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', TokenObtainPairView.as_view(), name='login'),

]