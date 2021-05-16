'use strict'

// server js file

// express module for server stuff
const express = require("express");

// use fetch api
const fetch = require("node-fetch");

// express object
const app = express();

// api key?
const API_KEY = process.env['API_KEY'];

// json-ify things
app.use(express.json());

// 'public' files are available
app.use(express.static('public'));


app.get("/weather/:lat/:long", async (request, response) => {
  let lat = request.params.lat;
  let lon = request.params.long;

  //make da api url
  //let url = `https://api.openweathermap.org/data/2.5/weather?q=${city_name}&appid=${API_KEY}`;

  let url = `https://api.openweathermap.org/data/2.5/weather?lat=${lat}&lon=${lon}&appid=${API_KEY}&units=imperial`;

  console.log("recieved the weather reqest");

  // do da fetch
  let fetch_response = await fetch(url);
  let json = await fetch_response.json();

  console.log("json", json);
  response.json(json);
})

// listen for requests :)
const listener = app.listen(3000, () => {
  console.log("The static server is listening on port " + listener.address().port);
});

