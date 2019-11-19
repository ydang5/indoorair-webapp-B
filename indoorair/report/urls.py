from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from homepage import views

urlpatterns = [
    path('report', views.report_list_page,name='report_list_page'),
    path('report/1', views.report_01_page,name='report_01_page'),
    path('report/api/1', views.download_csv_report_01_temperature_sensor_api.,name ='download_csv_report_01_api'),
]

urlpatterns = format_suffix_patterns(urlpatterns)
