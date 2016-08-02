function redirectToLogin() {
    window.location.replace("/login");
}

function redirectToEvent(){
    window.location.replace("/createEvent")
}

function redirectToSearch(){
    window.location.replace("/search")
}

 // var reader = new window.FileReader();
 // reader.readAsDataURL(blob); 
 // reader.onloadend = function() {
 //                base64data = reader.result;                
 //                console.log(base64data );
 //  }

function setup() {
    $("#login").click(redirectToLogin);
    $("#event").click(redirectToEvent);
    $('#search').mouseenter(redirectToSearch);
}
$(document).ready(setup)