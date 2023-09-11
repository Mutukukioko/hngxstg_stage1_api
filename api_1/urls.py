from django.urls import path
from . import views

urlpatterns = [
       path('api/<str:slack_name>/<str:track>/', views.api_endpoint, name='api_endpoint'),

]
