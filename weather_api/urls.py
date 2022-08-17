from django.urls import re_path, path
from drf_yasg import openapi
from drf_yasg.views import get_schema_view

from weather_api.views import WeatherInfoAPIView

schema_view = get_schema_view(
    openapi.Info(
        #  add your swagger doc title
        title="YOYO WEATHER API",
        #  version of the swagger doc
        default_version='v1',
        # first line that appears on the top of the doc
        description="Returns temperature data for a specific city within a range of days",
    ),
    public=True,
)

urlpatterns = [

    path('locations/<str:city>/', WeatherInfoAPIView.as_view(),
         name='temperature-info'),
    path('docs/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui')
]
