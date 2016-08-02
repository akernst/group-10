function redirectToLogin() {
    window.location.replace("/login");
}

function redirectToEvent(){
    window.location.replace("/createEvent")
}

function setup() {
    $("#login").click(redirectToLogin);
    $("#event").click(redirectToEvent);
}
$(document).ready(setup)