from django.urls import path
from .views      import Write, WriteDetail

urlpatterns = [
    path('', Write.as_view()),
    path('/<int:pk>',WriteDetail.as_view())
]
