from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from . import views

urlpatterns = [
    path('sensor/<int:id>', views.sensor_retrieve_page, name='sensor_retrieve_page'),
    path('api/sensor/<int:id>', views.SensorRetrieveAPI.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
