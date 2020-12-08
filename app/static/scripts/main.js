function enterPressed() {
    document.getElementById('Input')
        .addEventListener('keyup', function(event) {
        event.preventDefault();
        if (event.keyCode === 13) {
            document.getElementById('convertButton').click();
            document.getElementById('Output').textContent = "{{ result }}";
        }});
}


function buttonClick() {
    document.getElementById('Output').textContent = "{{ result }}";
}

function main() {
  document.getElementById("convertButton").addEventListener("click", buttonClick);
}

document.addEventListener("DOMContentLoaded", main);
