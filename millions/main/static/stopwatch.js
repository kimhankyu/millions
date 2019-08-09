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

function printClock() {

    var clock = document.getElementById("clock");            // 출력할 장소 선택
    var currentDate = new Date();                                     // 현재시간
    var calendar = currentDate.getFullYear() + "-" + (currentDate.getMonth()+1) + "-" + currentDate.getDate() // 현재 날짜
    var amPm = 'AM'; // 초기값 AM
    var currentHours = addZeros(currentDate.getHours(),2); 
    var currentMinute = addZeros(currentDate.getMinutes() ,2);
    var currentSeconds =  addZeros(currentDate.getSeconds(),2);

    if(currentHours >= 12){ // 시간이 12보다 클 때 PM으로 세팅, 12를 빼줌
        amPm = 'PM';
        currentHours = addZeros(currentHours - 12,2);
    }

    if(currentSeconds >= 50){// 50초 이상일 때 색을 변환해 준다.
       currentSeconds = '<span style="color:#de1951;">'+currentSeconds+'</span>'
    }
    clock.innerHTML = currentHours+":"+currentMinute+":"+currentSeconds +" <span style='font-size:50px;'>"+ amPm+"</span>"; //날짜를 출력해 줌

    setTimeout("printClock()",1000);         // 1초마다 printClock() 함수 호출
}

function addZeros(num, digit) { // 자릿수 맞춰주기
      var zero = '';
      num = num.toString();
      if (num.length < digit) {
        for (i = 0; i < digit - num.length; i++) {
          zero += '0';
        }
      }
      return zero + num;
}
