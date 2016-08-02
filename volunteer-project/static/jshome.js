

function redirectToEvent(){
    window.location.replace("/createEvent")
}

function redirectToSearch(){
    window.location.replace("/search")
}

function redirectToHome(){
	alert("Thanks for submitting your event! It is now added to our database.")
	window.location.replace("/")
}

function setup() {

    $(".event").click(redirectToEvent);
    $("#createform").click(redirectToHome)
}

$(document).ready(setup)