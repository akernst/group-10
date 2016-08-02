

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
  	data: { id : 1234 },
});
}

 function setup() {

    $(".event").click(redirectToEvent);
    $("#createform").submit(printThanks)
    $(".register").click(signUp)
 }

$(document).ready(setup)