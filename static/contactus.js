function myMap() {
    contentString = '<h5 id="developer">Developed by Ayush Agarwal</h5><h5 id="college">Amity University, Noida (India)</h5>'
    var mapOptions = {
        center: new google.maps.LatLng(28.544009, 77.332988),
        zoom: 13,
        mapTypeId: google.maps.MapTypeId.ROADMAP
    }
    var map = new google.maps.Map(document.getElementById("map"), mapOptions);
    var myLatLng = {lat: 28.544009, lng: 77.332988};
    var marker = new google.maps.Marker({
        position: myLatLng,
        map: map,
    });
    var infowindow = new google.maps.InfoWindow({
        content: contentString
    });
    marker.addListener('click', function() {
        infowindow.open(map, marker);
    });
}