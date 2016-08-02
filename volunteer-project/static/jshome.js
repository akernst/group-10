function redirectToLogin() {
    window.location.replace("/login");
}

function redirectToEvent(){
    window.location.replace("/createEvent")
}

<<<<<<< HEAD
=======
function redirectToSearch(){
    window.location.replace("/search")
}


>>>>>>> ad9904e712032fcaa388d814632dd895c0885c00
function setup() {
    $("#login").click(redirectToLogin);
    $("#event").click(redirectToEvent);
    $('#search').mouseenter(redirectToSearch);
}
$(document).ready(setup)