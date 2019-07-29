let seconds = 0;
let minutes = 0;
let hours = 0;

//Define vars to hold "display" value
let displaySeconds = 0;
let displayMinutes = 0;
let displayHours = 0;

//Define var to hold setInterval() function
let interval = null;

//Define var to hold stopwatch status
let status = "stopped";

//Stopwatch function (logic to determine when to increment next value, etc.)
function stopWatch() {
    seconds++;

    //Logic to determine when to increment next value
    if (seconds / 60 === 1) {
        seconds = 0;
        minutes++;

        if (minutes / 60 === 1) {
            minutes = 0;
            hours++;
        }
    }
    //If seconds/minutes/hours are only one digit, add a leading 0 to the value
    if (seconds < 10) {
        displaySeconds = "0" + seconds.toString();
    }
    else {
        displaySeconds = seconds;
    }

    if (minutes < 10) {
        displayMinutes = "0" + minutes.toString();
    }
    else {
        displayMinutes = minutes;
    }

    if (hours < 10) {
        displayHours = "0" + hours.toString();
    }
    else {
        displayHours = hours;
    }

    //Display updated time values to user
    var returnTime = displayHours + ":" + displayMinutes + ":" + displaySeconds;
    document.getElementById("display").innerHTML = returnTime;
    return returnTime;
}

function postRequest(url, data) {
    return fetch(url, {
        credentials: 'same-origin', // 'include', default: 'omit'
        method: 'POST', // 'GET', 'PUT', 'DELETE', etc.
        body: JSON.stringify(data), // Coordinate the body type with 'Content-Type'
        headers: new Headers({
            'Content-Type': 'application/json'
        }),
    })
        .then(response => response.json())
}


function startStop() {
    if (status === "stopped") {
        //Start the stopwatch (by calling the setInterval() function)
        let str;
        interval = window.setInterval(function () {
            str = stopWatch();
        }, 1000);
        postRequest('millions/main/views.py', str);
        document.getElementById("startStop").innerHTML = "Stop";
        status = "started";
    }
    else {
        window.clearInterval(interval);
        document.getElementById("startStop").innerHTML = "Start";
        status = "stopped";

    }
}

//Function to reset the stopwatch
function reset() {
    window.clearInterval(interval);
    seconds = 0;
    minutes = 0;
    hours = 0;
    document.getElementById("display").innerHTML = "00:00:00";
    document.getElementById("startStop").innerHTML = "Start";

}

function record() {
    window.clearInterval(interval);

    const p = document.createElement('p');
    p.innerHTML = time.toFixed(2);
    recordsArea.appendChild(p);
}