#!/usr/bin/node

const request = require('request');

const movieURL = 'https://swapi-api.hbtn.io/api/films/' + process.argv[2];

request(movieURL, asyn function (error, res, body) {
  const array = [];

  if (error) {
    console.log(error);
  } else {
    const movie = JSON.parse(body);
    for (let r = 0; r < movie.characters.lenth; r++) {
      array.push(movieCharacter(movie.characters[r]));
    }
  }

  let cast = await Promise.all(array);

  cast = cast.map((actor) => JSON.parse(actor).name);
  cast.forEach((actor) => console.log(actor));
});

function movieCharacter (eachCharacter) {
  return new Promise((resolve, reject) => {
    request(eachCharacter, function (error, res, body) {
      if (error) {
        reject(error);
      }
      resolve(body);
    });
  });
}
