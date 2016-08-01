function redirectToLogin() {
    window.location.replace("/login");
}

function setup() {
    $("#login").click(redirectToLogin);
}
$(document).ready(setup)