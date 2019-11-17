function onCreateClick() {
    window.location.href = "{% url 'instrument_create_page' %}";
}

function onBackClick() {
    window.location.href = "{% url 'dashboard_page' %}";
}

/**
 * STEP 4:
 * The purpose of this function is to take the 'model'
 * data received by the 'API web-service' and update
 * this page's `view`. The `view` we are modifying
 * is the HTML table.
 */
function generateTableFromObject(dataObj) {
    // This is the code which will create
    // the table header row.
    var htmlText = "<tr>";
    htmlText += "<th>ID</th>";
    htmlText += "<th>Name</th>";
    htmlText += "<th></th>";
    htmlText += "</tr>";

    // This is the code which will generate
    // all the rows from the data from the
    // API endpoint.

    const instrumentsArray = dataObj.instruments;
    for (instrumentObj of instrumentsArray) {
        var idString = instrumentObj.id.toString();
        console.log(idString);
        htmlText += "<tr>";
        htmlText += "<td>"+idString+"</td>";
        htmlText += "<td>"+instrumentObj.name+"</td>"
        htmlText += "<td>";
        htmlText += "<button onclick='onViewClick("+idString+");'>View</button>";
        htmlText += "</td>";
        htmlText += "</tr>";
    }

    var tableElement = document.getElementById("instruments_list");
    tableElement.innerHTML = htmlText;
}

/**
 * STEP 2: We need to create a function to `GET` the
 *         list data from the API web-service
 */
function onPageLoadRunGetInstrumentsListFromAPI() {
    var xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function() {
        if (this.readyState == 4 && this.status == 200) {
            const dataString = this.responseText;
            const dataObj = JSON.parse(dataString);

            /*
             *  STEP 3: We need to input the JavaScript Object
             *          into somesort of function which will
             *          generate the HTML table based on the
             *          object data
             */
            generateTableFromObject(dataObj);
        }
    }
    xhttp.open("GET","api/instruments", true);
    xhttp.send();
}

onPageLoadRunGetInstrumentsListFromAPI();

function onViewClick(instrumentId) {
    window.location.href = "/instrument/"+instrumentId;
}
