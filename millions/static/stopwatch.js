let seconds = 0;
let minutes = 0;
let hours = 0;
let str;
//Define vars to hold "display" value
let displaySeconds = 0;
let displayMinutes = 0;
let displayHours = 0;

//Define var to hold setInterval() function
let interval = null;

//Define var to hold stopwatch status
let status = "stopped";

function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie != '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) == (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
var csrftoken = getCookie('csrftoken');

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

function startStop() {
    if (status === "stopped") {
        //Start the stopwatch (by calling the setInterval() function)
        interval = window.setInterval(function () {
            str = stopWatch();
        }, 1000);
        status = "started";
    }
    else {
        console.log(str);
        window.clearInterval(interval);
        status = "stopped";
        fetch('http://127.0.0.1:8000', {
            method: 'post',
            headers: {
                "X-CSRFToken": getCookie("csrftoken"),
                "Accept": "application/json",
                "Content-Type": "application/json"                
            },
            body: JSON.stringify({data:str})
          }).then(function(response) {
            var aa = response.json();
            console.log(aa);
            return aa;
          });
    }
}