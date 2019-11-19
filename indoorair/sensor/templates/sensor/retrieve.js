function onPageLoadCallSensorRetrieveAPI(instrument_id) {
    var xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function() {
        if (this.readyState == 4 && this.status == 200) {
            const dataString = this.responseText;
            const dataObj = JSON.parse(dataString);
            generateViewFromObject(dataObj);
        }
    }
    const detailURL = "/api/sensor/"+sensor_id.toString();
    console.log(detailURL);
    xhttp.open("GET", detailURL, true);
    xhttp.send();
}

const sensor_id = {{ sensor_id }};
onPageLoadRunGetInstrumentDetailsFromAPI(sensor_id);

function renderPageWithData(dataObj){
    var idElement = document.getElementById('sensor_id');
    var nameElement = document.getElementById('sensor_name');
    idElement.innerHTML = dataObj.id
    nameElement.innerHTML = dataObj.name
}

function onBackClick() {
    window.location.href = "{% url 'i_retrieve_page' %}";
}
