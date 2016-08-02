

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

function signUp(event){

	console.log(event.target.dataset.eventid)
	var request = $.ajax({
  	url: "/allEvents",
  	method: "POST",
  	data: { id : event.target.dataset.eventid},
});
}

 function setup() {

    $(".event").click(redirectToEvent);
    $("#createform").submit(printThanks)
    $(".register").click(signUp)
 }

$(document).ready(setup)