import os

import requests
from django.http import JsonResponse
from django.shortcuts import redirect
from dotenv import load_dotenv
# Create your views here.
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.views import APIView

from weather_api.serializers import TemperatureSerializer
from weather_api.utilities import get_temp_info

load_dotenv()


class WeatherInfoAPIView(APIView):
    """Temperature Stats are Retrieved and Processed via this end point"""

    days = openapi.Parameter('days', in_=openapi.IN_QUERY,
                             type=openapi.TYPE_INTEGER, required=True)

    FETCH_TEMP_SUCCESS = '''{
        "city": <location>, 
        "days": <days>,
        "maximum": <maximum>,
        "minimum": <minimum>,
        "median": <median>,
        "average":<average>,
       
    }'''

    @action(methods=['GET'], detail=True)
    @swagger_auto_schema(
        manual_parameters=[days],
        responses={200: FETCH_TEMP_SUCCESS}
    )
    def get(self, request, city) -> Response:
        days = request.query_params.get('days', None)
        if not days:
            return Response('days parameter is missing', status=status.HTTP_400_BAD_REQUEST)

        base_url = os.getenv('WEATHER_URL')
        api_key = os.getenv('API_KEY')

        if not base_url and api_key:
            return Response('Credentials missing', status=status.HTTP_400_BAD_REQUEST)

        final_url = f'{base_url}forecast.json?key={api_key}&q={city.capitalize()}&days={days}'
        response = requests.get(final_url)
        data = response.json()
        if response.status_code != 200:
            return Response(data["error"]["message"], status=response.status_code)

        temperature_info = get_temp_info(data, days, city)
        serializer = TemperatureSerializer(temperature_info)

        return Response(serializer.data, status=status.HTTP_200_OK)


def docs(request):
    return redirect('/api/docs')
