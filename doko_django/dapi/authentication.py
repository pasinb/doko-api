from rest_framework import authentication
from rest_framework import exceptions
from django.conf import settings
from .models import  *
from requests.exceptions import HTTPError

class FirebaseAuth(authentication.BaseAuthentication):
    def authenticate(self, request):
        firebase = settings.FIREBASE
        auth = firebase.auth()
        if request.GET.get('dev') is not None:
            response =  auth.sign_in_with_email_and_password("testdoko@gmail.com", "testdoko")
            userObj, created = FirebaseUser.objects.get_or_create(
                id=response['idToken'],
            )
            return (userObj, None)

        try:
            header = request.META['HTTP_AUTHORIZATION']
        except KeyError:
            raise exceptions.AuthenticationFailed('AuthenticationFailed (No Auth Header provided)')
        if header[:5] != "Doko ":
            raise exceptions.AuthenticationFailed('AuthenticationFailed (Invalid Header)')
        try:
            response = auth.get_account_info(header[5:])
        except HTTPError as e:
            print('invalid token: '+str(e))             
            raise exceptions.AuthenticationFailed('AuthenticationFailed (Token Invalid)')
            
        userId = response["users"][0]["localId"]
        userObj, created = FirebaseUser.objects.get_or_create(
            id=userId,
        )
        
        return (userObj, None)