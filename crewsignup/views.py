from django.shortcuts import render
from django.shortcuts import render
from rest_framework import viewsets
from .serializers import *
from .models import *
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import RetrieveAPIView, ListAPIView, GenericAPIView, CreateAPIView
from rest_framework.response import Response
from rest_framework import status
from django.http import QueryDict


# Create your views here.


class UserView(CreateAPIView):
    allowed_methods = ['POST']
    serializer_class = UserSerializer

    def post(self, request, *args, **kwargs):
        temp = User(first_name=request.data.get('first_name', None),
                    last_name=request.data.get('last_name', None),
                    email=request.data.get('email', None),
                    phone_number=request.data.get('phone_number', None),
                    student_number=request.data.get('student_number', 0))
        if request.data.get('student_number') == '' or request.data.get('student_number') == None:
            temp.student_number = 0
        temp.save()

        return Response({"pk": temp.pk})


class AnswerListView(RetrieveAPIView):
    serializer_class = AnswerSerializer
    allowed_methods = ['GET']

    def get(self, request, *args, **kwargs):
        aid = kwargs['answer_id']
        a = Answer.objects.filter(pk=aid)
        adata = AnswerSerializer(instance=a, many=True).data
        return Response({'Answer': adata})

    # def post(self, request, *args, **kwargs):
    #     temp = Answer(
    #                   text=request.data.get('text', None),
    #                   boolean=request.data.get('boolean', None),
    #     )
    #     temp.save()

    # return Response({"status": "ok"})


class AnswerPostView(CreateAPIView):
    serializer_class = AnswerSerializer
    allowed_methods = ['POST', ]

    def post(self, request, *args, **kwargs):

        # temp = Answer(
        #     user=request.data.get('user', None),
        #     question=int(request.data.get('question', None)),
        #     text=request.data.get('text', None),
        #     boolean=request.data.get('boolean', None),
        # )
        # temp.save()


        serialized = AnswerSerializer(data=request.data, many=True)
        if serialized.is_valid():
            serialized.save()

        return Response({'response': 'ok'})


class ParentView(ListAPIView):
    serializer_class = ParentSerializer
    allowed_methods = ['GET']
    queryset = Parent.objects.all()


class CategoryView(ListAPIView):
    serializer_class = CategorySerializer
    allowed_methods = ['GET']
    queryset = Category.objects.all()


class QuestionView(ListAPIView):
    serializer_class = QuestionSerializer
    allowed_methods = ['GET']
    queryset = Question.objects.all()
