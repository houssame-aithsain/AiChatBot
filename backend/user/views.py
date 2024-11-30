from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action 
from django.http import HttpResponse

class UserViewSet(viewsets.ModelViewSet):

    @action(detail=False, methods=['GET'])
    def get(self, request):
        return Response("Hello, this is a simple string response", status=status.HTTP_200_OK)
