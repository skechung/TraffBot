'use strict'  // always start with this 

/* calculator button */
let calc_button = document.getElementById("calc");
calc_button.addEventListener("click", calc_duration);

/* make input blank */
document.getElementById("time-input").value = "";

/* lat, long */
let coord = [];

getLocation();

/* button to trigger the calculation and display it */
async function calc_duration() {

  let time = document.getElementById("time-input").value;

  if (!time) {
    alert("Please enter the start time of the crash!");
    return;
  }
  if (!coord[0] && !coord[1]) {
    alert("Please refresh and let us use your location");

  }
  else {

    console.log("coord", coord);

    //let hum_temp_wind = await get_weather(coord[0], coord[1]);

    // fake weather info
    let hum_temp_wind = [30, 40, 20];

    document.getElementById("calc-box").style.display = "none";
    document.getElementById("time-label").style.display = "none";
    document.getElementById("time-input").value = "";
    document.getElementById("time-input").style.display = "none";

    document.getElementById("result-box").style.display = "flex";
    model(coord[0], time, hum_temp_wind[1], hum_temp_wind[1], hum_temp_wind[2])
    .then(duration_in_mins => {
      document.getElementById("result").textContent = duration_in_mins.toString() + " minutes";
    })
  }
}

function getLocation() {
  if (navigator.geolocation) {
    navigator.geolocation.getCurrentPosition(showPosition);
  } else {
    alert("Geolocation is not supported by this browser.");
  }
}

function showPosition(position) {
  let lat = position.coords.latitude;
  let long = position.coords.longitude
  coord = [lat, long];
  console.log("in showPosition", lat, long);
}

/* gets the weather information and returns it in an arr
[hum, temp, wind] where humidity is in %, temp is F, wind in mph
NOTE: need to make an account to get the API key
and set it as an env var
*/
async function get_weather(lat, long) {

  let url = `/api/weather/${lat}/${long}`;

  // wait for the response
  let response = await fetch(url);

  // json the data
  let json = await response.json();

  let hum_temp_wind = [json["main"]["humidity"], json["main"]["temp"], json["wind"]["speed"]]
  return hum_temp_wind;
}

/* model function */
async function model(lat, time, hum, temp, wind) {

  // fake input
  let input = {
    "lat": lat,
    "time": time,
    "hum": hum,
    "temp": temp,
    "wind": wind,
  }

  console.log("about to fetch post ");

  // get the prediction
  return fetch (`/api/prediction`, {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify(input), // post body
  })
  .then(response => response.json())
  .then(data => {
      // do the model here
    console.log("data", data.data.prediction);
    return data.data.prediction;
  })
  .catch((error) => {
    console.error('Predition error in model:', error);
  });
  
}
