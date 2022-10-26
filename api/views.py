from rest_framework import viewsets
from .serializers import WeatherSerializer, WeatherInputSerializer
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
        
        # data = WeatherService.fetch(**inputSerializer.data)

        data = {
            "maximum": 1,
            "minimum": 1,
            "average": 1,
            "median": 1
        }

        print(f">>> Input {inputSerializer.data}")


        serializer = WeatherSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        return Response(serializer.data)