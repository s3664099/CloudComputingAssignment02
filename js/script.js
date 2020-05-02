var markers = new Array()

function initMap() {
  locationStatusText = document.getElementById("locationStatus");
  var map = new google.maps.Map(
   	document.getElementById('map'), {zoom: 15, center: {lat: -37.9604037, lng:144.7027854}});
    map.setOptions({styles: styles['hide']})

	if (navigator.geolocation) {
		navigator.geolocation.getCurrentPosition(function (position) {
			var pos = {
 	  			lat: position.coords.latitude,
      			lng: position.coords.longitude
       		};
		var marker = new google.maps.Marker({position: pos, map: map});
		locationStatusText.innerHTML = "Got location."
		});
	} else {
		locationStatusText.innerHTML = "Failed to get location.";
	}

	for (i = 0; i < locations.length; i++) {

	    var image = {
	  		url: 'https://storage.googleapis.com/map-icons-cca02/icons/'+locations[i].icon+'?authuser=2',
	  		scaledSize: new google.maps.Size(20,20),
	  		origin: new google.maps.Point(0,0),
	  		anchor: new google.maps.Point(0,32)
		};
	    var marker = new google.maps.Marker({position: {lat: locations[i].x_coord, lng: locations[i].y_coord }, 
	      	map: map,
	      	icon: image
	    })
	    markers.push(marker)
	}

    console.log(markers.length);
}
var styles = {
  	default: null,
 	hide: [
	{
  		featureType: 'poi',
  		stylers: [{visibility: 'off'}]
  	}]
};
	