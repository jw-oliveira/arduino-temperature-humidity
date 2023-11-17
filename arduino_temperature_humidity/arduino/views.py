from django.shortcuts import render, HttpResponse
from rest_framework import generics
from .models import Records
from .serializers import RecordsSerializer


def index(request):
    return HttpResponse('Hello World')


class RecordsCreateView(generics.CreateAPIView):
    queryset = Records.objects.all()
    serializer_class = RecordsSerializer

# Create your views here.
