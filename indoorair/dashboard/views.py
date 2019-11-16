import statistics

from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.shortcuts import redirect
from rest_framework import status, response, views
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User

from foundation.models import Instrument, Sensor, TimeSeriesDatum


def dashboard_page(request):
    user = request.user


    if user.is_authenticated == False:
        return HttpResponse("Cannot view page - you must login first")

    context = {
        'user': user,
    }
    return render(request,'dashboard/dashboard.html',context)


class DashboardAPIView(views.APIView):
    def get(self, request):
        return response.Response(
            status=status.HTTP_200_OK,
            data = {
                "average_temperature": get_average_temperature(),
                "average_pressure": get_average_pressure(),
                "average_co2": get_average_co2(),
                "average_tvoc": get_average_tvoc(),
                "average_humidity": get_average_humidity(),
            })
#http --form GET http://127.0.0.1:8000/api/dashboard

def get_average_temperature():
    sum = 0
    data = TimeSeriesDatum.objects.filter(sensor = "Temperature")
    for datum in data:
        sum = sum + datum.value
    try:
        output = sum/len(data)

        return output
    except Exception as e:
        return None

def get_average_pressure():
    sum = 0
    data = TimeSeriesDatum.objects.filter(sensor = "Pressure")
    for datum in data:
        sum = sum + datum.value
    try:
        output = sum/len(data)

        return output
    except Exception as e:
        return None


def get_average_co2():
    sum = 0
    data = TimeSeriesDatum.objects.filter(sensor = "CO2")
    for datum in data:
        sum = sum + datum.value
    try:
        output = sum/len(data)

        return output
    except Exception as e:
        return None


def get_average_tvoc():
    sum = 0
    data = TimeSeriesDatum.objects.filter(sensor = "TVOC")
    for datum in data:
        sum = sum + datum.value
    try:
        output = sum/len(data)

        return output
    except Exception as e:
        return None


def get_average_humidity():
    sum = 0
    data = TimeSeriesDatum.objects.filter(sensor = "Humidity")
    for datum in data:
        sum = sum + datum.value
    try:
        output = sum/len(data)

        return output
    except Exception as e:
        return None

class ListInstrumentAPIView(views.APIView):
    def get(self, request):
        if request.user.is_authenticated:
            try:
                Instrument.objects.get(id=1)
            except Exception as e:
                return response.Response(
                status=status.HTTP_404_NOT_FOUND,
                data = {
                    'message': 'Please add at least one insturment.',
                }
            )
            instruments = Insturment.objects.values('name')
            return response.Response(
                status=status.HTTP_200_OK,
                data={
                    'result': instruments,
                    'count':Instrument.objects.all().count()
                    }
                )
        else:
            return response.Response(
            status=status.HTTP_401_UNAUTHORIZED,
            data = {
                'message': 'Please log in.',
            }
        )
#http --form GET http://127.0.0.1:8000/api/list-instrument


class InstrumentSensorStatAPIView(views.APIView):
    def get(self, request):
        if request.user.is_authenticated:
            try:
                temperature_values = TimeSeriesDatum.objects.filter(sensor = "Temperature").values_list('value', flat=True)
                pressure_values = TimeSeriesDatum.objects.filter(sensor = "Pressure").values_list('value', flat=True)
                co2_values = TimeSeriesDatum.objects.filter(sensor = "CO2").values_list('value', flat=True)
                tvoc_values = TimeSeriesDatum.objects.filter(sensor = "TVOC").values_list('value', flat=True)
                humidity_values = TimeSeriesDatum.objects.filter(sensor = "Humidity").values_list('value', flat=True)


                return response.Response(
                    status=status.HTTP_200_OK,
                    data = {
                        'temperature mean':statistics.mean(temperature_values),
                        'pressure mean':statistics.mean(pressure_values),
                        'co2 mean':statistics.mean(co2_values),
                        'tvoc mean':statistics.mean(tvoc_values),
                        'humidity mean':statistics.mean(humidity_values),
                        'temperature median':statistics.median(temperature_values),
                        'pressure median':statistics.median(pressure_values),
                        'co2 median':statistics.median(co2_values),
                        'tvoc median':statistics.median(tvoc_values),
                        'humidity median':statistics.median(humidity_values),
                        'temperature mode':statistics.mode(temperature_values),
                        'pressure mode':statistics.mode(pressure_values),
                        'co2 mode':statistics.mode(co2_values),
                        'tvoc mode':statistics.mode(tvoc_values),
                        'humidity mode':statistics.mode(humidity_values),
                    }
                )
            except Exception as e:
                return response.Response(
                    status=status.HTTP_500_INTERNAL_SERVER_ERROR,
                    data = {
                        'error':str(e)
                    }
                )
        else:
            return response.Response(
            status=status.HTTP_401_UNAUTHORIZED,
            data = {
                'message': 'Please log in.',
            }
        )
