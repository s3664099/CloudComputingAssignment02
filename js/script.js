var markers = new Array();
var iconSize = false;
var iconShown = false;
var smallIcon = 20;
var largeIcon = 40;
var longitude = -37.8165686;
var latitude = 144.9805071;

function initMap() {
  locationStatusText = document.getElementById("locationStatus");

	if (navigator.geolocation) {
		navigator.geolocation.getCurrentPosition(function (position) {
			var pos = {
 	  			lat: position.coords.latitude,
      			lng: position.coords.longitude
       		};
		var marker = new google.maps.Marker({position: pos, map: map});
		locationStatusText.innerHTML = "Got location.";
		console.log("Got location");
		latitude = pos.lat;
		longitude = pos.lng;
		});
	} else {
		locationStatusText.innerHTML = "Failed to get location.";
		console.log("Failed to get location");
	}

  var map = new google.maps.Map(
   	document.getElementById('map'), {zoom: 15, center: {lat: longitude, lng:latitude}});
    map.setOptions({styles: styles['hide']})

	for (i = 0; i < locations.length; i++) {

	    var image = setIcons(locations[i].icon, smallIcon);
	    var marker = new google.maps.Marker({position: {lat: locations[i].x_coord, lng: locations[i].y_coord }, 
	      	map: map,
	      	icon: image
	    })
	    marker.setMap(null);
	    markers.push(marker);
	}

	map.addListener('zoom_changed', function() {
		zoom = map.getZoom();

		if (zoom >14 && zoom < 18 && (iconShown == false || iconSize == true)) {
			setIconImage(true)
			setMapOnAll(map);
			iconSize = false;
			iconShown = true;
		} else if (zoom >17 && iconSize == false) {
			setIconImage(false)
			setMapOnAll(map);
			iconSize = true
		} else if (zoom <15) {
			setMapOnAll(null);
			iconShown = false;
		}
	});
}

var styles = {
  	default: null,
 	hide: [
	{
  		featureType: 'poi',
  		stylers: [{visibility: 'off'}]
  	}]
};

function setIcons(icon, size) {

	var image = {
	  		url: 'https://storage.googleapis.com/map-icons-cca02/icons/'+icon+'?authuser=2',
	  		scaledSize: new google.maps.Size(size,size),
	  		origin: new google.maps.Point(0,0),
	  		anchor: new google.maps.Point(0,32)
		};
	return image;
}

function setIconImage(size) {

	iconSize = largeIcon;

	if(size) {
		iconSize = smallIcon;
	}

	for (var i=0; i<markers.length; i++) {

		var image = setIcons(locations[i].icon, iconSize);
		markers[i].setIcon(image);
	}

}


function setMapOnAll(map) {
	for (var i = 0; i<markers.length; i++) {
		markers[i].setMap(map);
	}
}