const apiKey = 'pk.eyJ1Ijoib2NhbGFrIiwiYSI6ImNsZDRpdDdqNjBzdnYzeW9hOHVsdGU1Y24ifQ.-Wjo_wt1binD7ALh--LIxQ'

const map = L.map('map').setView([51.514244,7.468429], 13);


L.tileLayer('https://tile.openstreetmap.org/{z}/{x}/{y}.png', {
    maxZoom: 19,
    attribution: '&copy; <a href="http://www.openstreetmap.org/copyright">OpenStreetMap</a>',
    accessToken: apiKey

}).addTo(map);


const marker = L.marker([51.514244,7.468429]).addTo(map);


let template = ` <h3>Kaiser Straße</h3>
<div style="text-align:center">
  <img width ="100" height="100"src="image.jpg"/> 
 </div>
`
let template1 = ` <h3>Iko Straße</h3>
`
marker.bindPopup(template);

const marker1 = L.marker([51.514244,7.478429]).addTo(map);
marker1.bindPopup(template1);


const circle = L.circle([51.514244,7.468429],{
    radius:1000,
    color : 'blue',
    fillColor : 'red',
    fillOpacity: 0.1
}).addTo(map)

