#!/usr/bin/node
const request = require('request');

if (process.argv[2]) {
  const options = {
    url: `https://swapi-api.alx-tools.com/api/films/${process.argv[2]}/`,
    method: 'GET'
  };

  request(options, function (err, res, body) {
    if (err) {
      console.log(err);
    } else if (res.statusCode === 200) {
      const characters = JSON.parse(res.body).characters;
      for (const character of characters) {
        // console.log(character.slice(43, character.length));
        const opt = {
          url: character,
          method: 'GET'
        };
        request(opt, function (err, res, body) {
          if (err) {
            console.log(err);
          } else if (res.statusCode === 200) {
            console.log(JSON.parse(body).name);
          }
        });
      }
    }
  });
//   let url = `https://swapi-api.alx-tools.com/api/films/${process.argv[2]}/`;
//   url = `https://swapi-api.alx-tools.com/api/films/`;
//   console.log(url.slice(42, 43))
}
