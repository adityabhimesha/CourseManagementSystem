from django.shortcuts import render

def index(request):
    return render(request, "react-header.html")


from rest_framework.views import APIView
from rest_framework import authentication, permissions
from django.core import serializers
from django.http import JsonResponse


class get_user_info(APIView):
    authentication_classes = [authentication.SessionAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, format=None):
    
        data = {
            'first_name' : request.user.first_name,
            'last_name' : request.user.last_name,
            'email' : request.user.email,
        }
        return JsonResponse(data)
