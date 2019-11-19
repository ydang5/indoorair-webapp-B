function downloadTemperatureDataOnClick(){
  window.location.href = "{% url 'download_csv_report_01_temperature_sensor_api' %};
}
