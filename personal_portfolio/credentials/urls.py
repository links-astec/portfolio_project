from django.urls import path
from . import views

urlpatterns = [
    path('projects/credentials/', views.Credential.as_view(),name='credential')
]
