from rest_framework.serializers import ModelSerializer

from .models import Question, Category

class QuestionSerializer(ModelSerializer):
    class Meta:
        model = Question
        fields = ['id', 'question', 'answer', 'category', 'difficulty']

class CategorySerializer(ModelSerializer):
    class Meta: 
        model = Category
        fields = ['id', 'type']