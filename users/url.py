from django.urls import path

from .views import ListCreateView, ReadUpdateDelete
urlpatterns = [
    path('', ListCreateView.as_view()),
    path('/<int:pk>', ReadUpdateDelete.as_view())
]