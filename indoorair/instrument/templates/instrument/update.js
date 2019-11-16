function onUpdateClick(){
const updateInsrtumentName = document.getElementById('update_instrument_name').value;
const updateInsrtumentUser = document.getElementById('update_instrument_user').value;
var xhttp = new XMLHttpRequest();
 xhttp.onreadystatechange = function() {
   if (this.readyState == 4 && this.status == 200) {
    document.getElementById("update").innerHTML = this.responseText;
   }
 };
 xhttp.open("POST", '/instrument/update/api', true);
 xhttp.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
 xhttp.send('update_instrument_name='+updateInsrtumentName+'&update_instrument_user='+updateInsrtumentUser);
}
