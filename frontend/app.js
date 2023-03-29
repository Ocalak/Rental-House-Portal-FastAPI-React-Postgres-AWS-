// Import the pg library
const { Client } = require('pg');


// Connect to the PostgreSQL database
const client = new Client({
    user: 'postgres',
    host: 'localhost',
    database: 'xxxxx',
    password: 'xxxxxx',
    port: 5432,
});

client.connect();

// Create a new Leaflet map with default options
const map = new google.maps.Map(document.getElementById("map"), {
    center: { lat: 40.7128, lng: -74.0060 },
    zoom: 10,
  });

// Retrieve the house coordinates from the database and add markers to the map
client.query('SELECT * FROM house WHERE lat IS NOT NULL AND lng IS NOT NULL', (err, res) => {
  if (err) {
    console.error(err);
  } else {
    res.rows.forEach(row => {
      const { lat, lng, adress } = row;
      const marker = map.marker([lat, lng]).addTo(map);
      marker.bindPopup(adress);
    });
  }
});

houses.forEach((house) => {
    const marker = new google.maps.Marker({
      position: { lat: house.lat, lng: house.lng },
      map: map,
      title: house.adress,
    });
  });
  
