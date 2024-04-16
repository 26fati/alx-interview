#!/usr/bin/node

const request = require('request');

const id = process.argv[2];

const url = `https://swapi-api.alx-tools.com/api/films/${id}/`;

request(url, (error, response, body) => {
  if (error) console.log(error);
  const data = JSON.parse(body);
  const characters = data.characters;

  function getCharacterName (url) {
    return new Promise((resolve, reject) => {
      request(url, function (error, response, body) {
        if (error) {
          reject(error);
          return;
        }
        const characterData = JSON.parse(body);
        resolve(characterData.name);
      });
    });
  }

  Promise.all(characters.map(getCharacterName))
    .then(names => {
      names.forEach(name => console.log(name));
    })
    .catch(error => {
      console.error('Error retrieving character names:', error);
    });
});
