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

    $(".login").click(redirectToLogin);
    $(".event").click(redirectToEvent);
    $('#search').mouseenter(redirectToSearch);
    $("#search").keyup(function(e) {
        if (e.which == 13) {
            window.location.replace("/search");
        }
   });
}
$(document).ready(setup)