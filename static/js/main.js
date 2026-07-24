


document.addEventListener("DOMContentLoaded", function() {

/* Display character count while writing message */
    const messageBody = document.querySelector("#messageBody");
    const charCounter = document.querySelector("#charCounter");

    if (messageBody && charCounter) {

        //Display initial counter
        charCounter.textContent = `${messageBody.value.length} characters`;


        //Update count when user types
        messageBody.addEventListener("input", function() {
            charCounter.textContent = `${messageBody.value.length} characters`;

        });
    }

/* Confimation message for buttons */
const confirmButtons = document.querySelectorAll(".confirm-action")
;

confirmButtons.forEach(function (button) {
button.addEventListener("click", function (event) {
const confirmed = confirm("Are you sure you want to do that?");

// Stop action is user cancels confirm dialogue

if (!confirmed) {
    event.preventDefault();
}

});
});
});

