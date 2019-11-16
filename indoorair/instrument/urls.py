from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from . import views

urlpatterns = [
    path('instrument/create', views.instrument_create_page, name='instrument_create_page'),
    path('instrument/list', views.instrument_list_page, name='instrument_list_page'),
    path('instrument/retrieve', views.instrument_retrieve_page, name='instrument_retrieve_page'),
    path('instrument/update', views.instrument_update_page, name='instrument_update_page'),
    path('instrument/create/api', views.InstrumentCeateAPI.as_view()),
    path('instrument/list/api', views.InstrumentListAPIView.as_view()),
    path('instrument/api/<id>', views.InstrumentRetrieveUpdateAPI.as_view()),
]
