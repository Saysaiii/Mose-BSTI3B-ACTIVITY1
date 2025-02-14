
from django.urls import path
from .views import index, about, project, contact

app_name = "portfolio"

urlpatterns = [
    path('', index, name='index'), 
    path('about/', about, name='about'),
    path('project/', project, name='project'),
    path('contact/', contact, name='contact'),
]

