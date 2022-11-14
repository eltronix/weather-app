from .serializers import ForecastSerializer, ForecastInputSerializer
from .services import WeatherService
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import Http404

class ForecastDetail(APIView):

    def get(self, request, city):
        input_data = {
            "city": city,
            "days": request.query_params.get("days", 1)
        }

        inputSerializer = ForecastInputSerializer(data = input_data)
        inputSerializer.is_valid(raise_exception=True)
        
        try:
            data = WeatherService.fetch_forecast(**inputSerializer.data)
        except:
            raise Http404

        serializer = ForecastSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        return Response(serializer.data)