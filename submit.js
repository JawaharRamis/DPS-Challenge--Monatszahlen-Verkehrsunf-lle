const axios = require('axios')
const hotpTotpGenerator = require('hotp-totp-generator')

const URL = 'https://dps-challenge.netlify.app/.netlify/functions/api/challenge';

const jsonBody = {
  github: 'https://github.com/JawaharRamis/DPS-Challenge--Monatszahlen-Verkehrsunf-lle/tree/master',
  email: 'jawaharramis@gmail.com',
  url: 'https://dps-challenge-jawahar.herokuapp.com/json',
  notes:
    'I have developed a simple UI running on flask server with a form to provide the input and return the model predictions at https://dps-challenge-jawahar.herokuapp.com.'+
    'The application is deployed on Heroku connected to the guthub repo to which Ihave added the requested files on to the master branch'
};

const password = hotpTotpGenerator.totp({
  key: 'Prateek.sawhney97@gmail.comDPSCHALLENGE',
  X: 120,
  T0: 0,
  algorithm: 'sha512',
  digits: 10
});

const headers = {
  'Content-Type': 'application/json',
  'Authorization': `Basic ${password}`
};

axios
  .post(URL, jsonBody, { headers })
  .then((response) => console.log('Response', response))
  .catch((error) => console.log('Error', error));