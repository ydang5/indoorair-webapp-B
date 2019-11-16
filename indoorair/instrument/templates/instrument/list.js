function onListClick(){

var xhttp = new XMLHttpRequest();
 xhttp.onreadystatechange = function() {
   if (this.readyState == 4 && this.status == 200) {
    document.getElementById("list").innerHTML = this.responseText;
   }
 };
 xhttp.open("GET", 'instrument/list/api', true);
 xhttp.send();
}
