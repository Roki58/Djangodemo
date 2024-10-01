from django.shortcuts import render
from django.http import HttpResponse
from .serializers import ProductSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
# Create your views here.

def index (request):
    return HttpResponse("Hello world, this is django ")

class ProductView(APIView):
    def post (self,request):
        serializer = ProductSerializer(data= request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status= status.HTTP_200_OK)
        return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)