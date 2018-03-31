from rest_framework import serializers
from .models import *


class CourseSer(serializers.ModelSerializer):
    # status = serializers.SerializerMethodField()

    # def get_status(self, obj):
    #     return Exam.STATUS[obj.status][1]

    class Meta():
        model = Course
        fields = ('__all__')


class SectionSer(serializers.ModelSerializer):
    class Meta:
        model = Section
        fields = ('__all__')


class QuestionSer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ('__all__')