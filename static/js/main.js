

/* Listener for confirm delete of project */
document.addEventListener("DOMContentLoaded", function() {


const confirmButtons = document.querySelectorAll(".confirm-adction")
;

confirmButtons.forEach(function (button) {
button.addEventListener("click", function (event) {
const confirmed = confirm("Are you sure you want to do that?");

if (!confirmed) {
    event.preventDefault();
}

});
});
});

