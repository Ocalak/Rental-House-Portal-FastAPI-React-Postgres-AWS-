const { Client } = require('pg');
const fetch = require('node-fetch');

const client = new Client({
  user: 'postgres',
  host: 'localhost',
  database: 'debug4',
  password: 'Ocal0151!',
  port: 5432,
});

async function updateHouseCoordinates() {
  try {
    await client.connect();
    const result = await client.query('SELECT * FROM house');
    const houses = result.rows;

    for (const house of houses) {
      const zipCode = house.zipcode;
      const url = `https://maps.googleapis.com/maps/api/geocode/json?address=DE${zipCode}&key=AIzaSyCiHUCayndjydekEx_zBbRMapM6cEAtQN4`;
      const response = await fetch(url);
      const data = await response.json();
      const location = data.results[0].geometry.location;
      const latitude = location.lat;
      const longitude = location.lng;
     

      await client.query('UPDATE house SET lat = $1, lng = $2  WHERE id = $3', [latitude, longitude, house.id]);
    }

    console.log('Coordinates updated successfully!');
  } catch (err) {
    console.error(err);
  } finally {
    await client.end();
  }
}

updateHouseCoordinates();
