#!/usr/bin/node

const request = require('request');
const url = process.argv[2];
request(url, function (error, response, body) {
  if (error) {
    console.log(error);
  }
  let list = [];
  for (const film of JSON.parse(body).results) {
    list = list.concat(film.characters);
  }
  const unique = list.filter(i => i.includes('18'));
  console.log(unique.length);
});
