import React, { useState, useEffect } from 'react';

function HouseTable() {
    const [houses, setHouses] = useState([]);

    useEffect(() => {
        fetch('http://127.0.0.1:8000/houses/all-houses')
            .then(response => response.json())
            .then(data => setHouses(data))
    }, []);

    return (<div className="min-h-screen  bg-yellow-500  flex justify-center items-center">
        <table>
            <thead>
                <tr>
                    <th>Address</th>
                    <th>City</th>
                    <th>title</th>
                    <th>Zipcode</th>
                    <th>Rent</th>
                </tr>
            </thead>
            <tbody>
                {houses.map(house => (
                    <tr key={house.id}>
                        <td>{house.adress}</td>
                        <td>{house.city}</td>
                        <td>{house.title}</td>
                        <td>{house.zipcode}</td>
                        <td>{house.rent}</td>
                    </tr>
                ))}
            </tbody>
        </table>
    </div>
    );
}

export default HouseTable;
