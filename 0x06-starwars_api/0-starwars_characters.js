#!/usr/bin/node
const request = require('request');

if (process.argv[2]) {
  function asyncGetData (url) {
    return new Promise((resolve, reject) => {
      request.get(url, function (err, res, body) {
        if (err) {
          resolve(err);
        } else if (res.statusCode !== 200) {
          reject(new Error(`status code: ${res.statusCode}`));
        } else {
          const data = JSON.parse(body);
          resolve(data);
        }
      });
    });
  }

  async function getData () {
    try {
      const url = `https://swapi-api.alx-tools.com/api/films/${process.argv[2]}/`;
      const data = await asyncGetData(url);
      const characters = data.characters;
      for (const character of characters) {
        const characterData = await asyncGetData(character);
        console.log(characterData.name);
      }
    } catch (err) {
      console.log(`err: ${err}`);
    }
  }

  getData();
}
