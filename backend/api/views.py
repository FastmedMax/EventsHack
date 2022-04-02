from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView

from .models import Review, Callback, Case, Event
from .serializers import ReviewSerializer, CaseSerializer, CaseFullSerializer, EventSerializer, CallBackSerializer

# Create your views here.
class RewiewListView(ListAPIView):
    queryset = Review
    serializer_class = ReviewSerializer

    def get(self, request, id=None, *args, **kwargs):
        try:
            if id:
                reviews = self.queryset.objects.filter(case=id)
            else:
                reviews = self.queryset.objects.order_by("?")[:5]
        except Review.DoesNotExist:
            return Response("Отзывы не найдены!", status=status.HTTP_404_NOT_FOUND)
        serializer = self.serializer_class(reviews, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class CaseListView(ListAPIView):
    queryset = Case
    serializer_class = CaseSerializer

    def get(self, request, *args, **kwargs):
        try:
            cases = self.queryset.objects.all()
        except Case.DoesNotExist:
            return Response("Кейсы не найден!", status=status.HTTP_404_NOT_FOUND)
        serializer = self.serializer_class(cases, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class CaseListBestView(ListAPIView):
    queryset = Case
    serializer_class = CaseSerializer

    def get(self, request, *args, **kwargs):
        try:
            cases = self.queryset.objects.filter(is_best=True)
        except Case.DoesNotExist:
            return Response("Кейсы не найден!", status=status.HTTP_404_NOT_FOUND)
        serializer = self.serializer_class(cases, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class CaseFullView(APIView):
    queryset = Case
    serializer_class = CaseFullSerializer

    def get(self, request, id):
        try:
            case = self.queryset.objects.get(id=id)
        except Case.DoesNotExist:
            return Response("Кейс не найден!", status=status.HTTP_404_NOT_FOUND)
        serializer = self.serializer_class(case)
        return Response(serializer.data, status=status.HTTP_200_OK)


class EventListView(ListAPIView):
    queryset = Event
    serializer_class = EventSerializer

    def get(self, request, id, *args, **kwargs):
        try:
            event = self.queryset.objects.get(id=id)
        except Event.DoesNotExist:
            return Response("События не найдены!", status=status.HTTP_404_NOT_FOUND)
        serializer = self.serializer_class(event)
        return Response(serializer.data, status=status.HTTP_200_OK)


class CallBackView(APIView):
    queryset = Callback
    serializer_class = CallBackSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid(raise_exception=False):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
