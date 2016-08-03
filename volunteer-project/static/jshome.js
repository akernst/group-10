

function redirectToEvent(){
    window.location.replace("/createEvent")
}

function redirectToSearch(){
    window.location.replace("/search")
}

function printThanks(){
	alert("Thanks for submitting your event! It is now added to our database.")
}

function signUp(){

	var request = $.ajax({
  	url: "/allEvents",
  	method: "POST",
  	data: { id : event.target.dataset.eventid},
});
  alert("Thank you for signing up! This event has been added to your events")
}

 function setup() {

    $(".event").click(redirectToEvent);
    $("#createform").submit(printThanks);
    $(".register").click(signUp)
 }

$(document).ready(setup)