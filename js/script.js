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
		
    {% for location in location_details %}
    x_coord = {{location.x_coord}};
    y_coord = {{location.y_coord}};
    icon = "{{location.icon}}";
    var image = {
  		url: 'https://storage.googleapis.com/map-icons-cca02/icons/'+icon+'?authuser=2',
  		scaledSize: new google.maps.Size(20,20),
  		origin: new google.maps.Point(0,0),
  		anchor: new google.maps.Point(0,32)
	};
    var marker = new google.maps.Marker({position: {lat: x_coord, lng: y_coord }, 
      	map: map,
      	icon: image
    })
    {% endfor %}
}
var styles = {
  	default: null,
 	hide: [
	{
  		featureType: 'poi',
  		stylers: [{visibility: 'off'}]
  	}]
};
	