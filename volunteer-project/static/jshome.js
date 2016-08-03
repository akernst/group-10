

function redirectToEvent(){
    window.location.replace("/createEvent")
}

function redirectToSearch(){
    window.location.replace("/search")
}

function printThanks(){
	alert("Thanks for submitting your event! It is now added to our database.")
	console.log()
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
    $("#createform").unbind('click').click(printThanks);
    $(".register").unbind('click').click(signUp)
 }

$(document).ready(setup)