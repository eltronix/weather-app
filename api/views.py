from rest_framework import viewsets
from .serializers import WeatherSerializer, WeatherInputSerializer
from .services import WeatherService
from rest_framework.views import APIView
from rest_framework.response import Response


class WeatherDetail(APIView):

    def get(self, request, city):
        input_data = {
            "city": city,
            "days": request.query_params.get("days", 1)
        }

        inputSerializer = WeatherInputSerializer(data = input_data)
        inputSerializer.is_valid(raise_exception=True)
        
        data = WeatherService.fetchForecast(**inputSerializer.data)

        serializer = WeatherSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        return Response(serializer.data)