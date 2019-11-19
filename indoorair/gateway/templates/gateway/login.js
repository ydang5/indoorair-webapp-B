function onLoginClick(){
  const usernameElement = document.getElementById("username");
  const username = usernameElement.value;
  console.log(username)
  const passwordElement = document.getElementById('password');
  const password = passwordElement.value;
  console.log(password);

  var xhttp = new XMLHttpRequest();
  xhttp.onreadystatechange = function(){
    if(this.readyState == 4 && this.status == 400){
        alert('username or password is incorrect!')
      }else if (this.readyState == 4 && this.status == 200){
          window.location.href = "/dashboard";
    }
  }
  xhttp.open("POST","/api/login", true);
  xhttp.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
  const string = "username=" + username+"&password=" +password
  xhttp.send(string)
}
