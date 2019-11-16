function onRetrieveClick(){
    const retrieveInsrtument = document.getElementById('retrieve_instrument').value;

    var xhttp = new XMLHttpRequest();
     xhttp.onreadystatechange = function() {
       if (this.readyState == 4 && this.status == 200) {
        document.getElementById("retrieve").innerHTML = this.responseText;
       }
     };
  xhttp.open('POST', '/instrument/retrieve/api', true);
  xhttp.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
  xhttp.send("retrieve_instrument="+retrieveInsrtument);
  }
