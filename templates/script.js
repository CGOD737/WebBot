//JavaScript Support for WebBot

//password toggle
function togglePW(){
    var x = document.getElementById("password")
    if(x.type == "password")
        x.type = "text";
    else
        x.type = "password";
}