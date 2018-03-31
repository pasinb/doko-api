from django.shortcuts import render
from rest_framework import viewsets, permissions, serializers
from django.conf import settings
from django.http import HttpResponseNotAllowed, HttpResponse, HttpResponseBadRequest, JsonResponse, HttpResponseForbidden
import json
from requests.exceptions import HTTPError
from .serializers import *

def get_users(request):
    firebase = settings.FIREBASE
    auth = firebase.auth()
    try:
        header = request.META['HTTP_AUTHORIZATION']
    except KeyError:
        return JsonResponse({'error':'auth header missing'}, status=403)
    if header[:5] != "Doko "   :
        return JsonResponse({'error':'invalid header format'}, status=403)
    try:
        response = auth.get_account_info(header[5:])
    except HTTPError as e:
        print('invalid token: '+str(e))
        return JsonResponse({'error':'token invalid'}, status=403)
        
    print(response["users"][0]["localId"])
    
    return HttpResponse(json.dumps(response))


def auth(request):
    firebase = settings.FIREBASE
    auth = firebase.auth()
    response =  auth.sign_in_with_email_and_password("testdoko@gmail.com", "testdoko")
    

    return HttpResponse(json.dumps(response))


class CourseVs(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSer

class SectionVs(viewsets.ModelViewSet):
    queryset = Section.objects.all()
    serializer_class = SectionSer

class QuestionVs(viewsets.ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSer
