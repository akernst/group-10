function redirectToLogin() {
    window.location.replace("/login");
}

function redirectToEvent(){
    window.location.replace("/createEvent")
}

function redirectToSearch(){
    window.location.replace("/search")
}
function setup() {
    $("#login").click(redirectToLogin);
    $("#event").click(redirectToEvent);
    $("#search").submit(redirectToSearch);
}
$(document).ready(setup)