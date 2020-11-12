document.getElementById("Input")
    .addEventListener("keyup", function(event) {
    event.preventDefault();
    if (event.keyCode === 13) {
        document.getElementById("convertButton").click();
    }
});

document.getElementById("convertButton").addEventListener("click", buttonClick);

function buttonClick() {
    document.getElementById("Output").value = "{{ value }}";
}
