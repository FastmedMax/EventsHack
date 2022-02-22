from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView

from .models import Review, Callback, Case, Event
from .serializers import ReviewSerializer, CaseSerializer, CaseFullSerializer, EventSerializer, CallBackSerializer

# Create your views here.
