
import React, { useEffect, useState } from 'react';
import GoogleMapReact from 'google-map-react';
import axios from 'axios';

const HouseMarker = ({ lat, lng }) => <div>🏠</div>;

function GoogleMap () {
  const [houses, setHouses] = useState([]);

  useEffect(() => {
    fetch('http://127.0.0.1:8000/houses/all-houses')
      .then(response => response.json())
      .then(data => setHouses(data))
  }, []);

  const center = { lat: 37.7749, lng: -122.4194 };
  const zoom = 12;

  return (
    <div style={{ height: '500px', width: '100%' }}>
      <GoogleMapReact
        bootstrapURLKeys={{ key: 'XXXXXXXXXXXXXXX' }}
        defaultCenter={center}
        defaultZoom={zoom}
      >
        {houses.map((house) => (
          <HouseMarker
            key={house.id}
            lat={house.lat}
            lng={house.lng}
          />
        ))}
      </GoogleMapReact>
    </div>
  );
};

export default GoogleMap;
