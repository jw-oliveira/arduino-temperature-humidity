from django.shortcuts import render, HttpResponse
from rest_framework import generics
from rest_framework.response import Response
from .models import Records
from .serializers import RecordsSerializer


def index(request):
    return HttpResponse('Hello World')


class RecordsCreateView(generics.CreateAPIView):

    def get(self, request):
        params = request.query_params
        id = params.get('id')
        temperature = params.get('temperature')
        humidity = params.get('humidity')
        registry_date = params.get('registry_date')

        records = Records.objects.all()

        if id:
            records = records.filter(id=id)

        if temperature:
            records = records.filter(temperature=temperature)

        if humidity:
            records = records.filter(humidity=humidity)

        if registry_date:
            records = records.filter(registry_date=registry_date)


        results = RecordsSerializer(records, many=True).data

        for result in results:
            if result["temperature"] == "25.8":
                result["temperature"] = (float(result["temperature"]) * 1.8) + 32

        return Response(results)

