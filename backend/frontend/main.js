let map;

function initMap() {
  map = new google.maps.Map(document.getElementById("map"), {
    center: { lat: 51.404, lng: 6.710 },
    zoom: 10,
  });
}
