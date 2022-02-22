from django.urls import path

from .views import RewiewListView,CaseListView, CaseFullView, CaseListBestView, EventListView, CallBackView

urlpatterns = [
    path("reviews/", RewiewListView.as_view()),
    path("reviews/<str:id>/", RewiewListView.as_view()),
    path("cases/", CaseListView.as_view()),
    path("cases/best/", CaseListBestView.as_view()),
    path("cases/<str:id>/", CaseFullView.as_view()),
    path("events/<str:id>/", EventListView.as_view()),
    path("callback/", CallBackView.as_view())
]