

/* Listener for confirm delete of project */
document.addEventListener("DOMContentLoaded", function() {

/* Wiring for message body character counter */
    const messageBody = document.querySelector("#messageBody");
    const charCounter = document.querySelector("#charCounter");

    if (messageBody && charCounter) {
        charCounter.textContent = `${messageBody.value.length} characters`;

        messageBody.addEventListener("input", function() {
            charCounter.textContent = `${messageBody.value.length} characters`;

        });
    }

const confirmButtons = document.querySelectorAll(".confirm-action")
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

