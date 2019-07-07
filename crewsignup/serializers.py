from rest_framework import serializers
from .models import *


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['pk', 'first_name', 'last_name', 'email', 'phone_number', 'student_number']


class ParentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Parent
        fields = ['pk', 'name']


class CategorySerializer(serializers.ModelSerializer):
    # parent = ParentSerializer()

    class Meta:
        model = Category
        fields = ['pk', 'parent', 'name']


class QuestionSerializer(serializers.ModelSerializer):
    # category = CategorySerializer()

    class Meta:
        model = Question
        fields = ['pk', 'category', 'text', 'is_bool']


class AnswerSerializer(serializers.ModelSerializer):
    # user = UserSerializer()
    # question = QuestionSerializer()

    class Meta:
        model = Answer
        fields = ['pk', 'user', 'question', 'text', 'boolean']
