from django.urls import path, include
from rest_framework import routers
from .views import *

urlpatterns = [
    path('user/', UserView.as_view()),
    path('answerlist/<int:answer_id>', AnswerListView.as_view()),
    path('answer/', AnswerPostView.as_view())
]
