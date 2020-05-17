//set up the variables
var markers = new Array();
var infowindows = new Array();
var iconSize = false;
var iconShown = false;
var smallIcon = 20;
var largeIcon = 40;
var longitude = -37.8165686;
var latitude = 144.9805071;

//initialise the Google Maps API
function initMap() {
  locationStatusText = document.getElementById("locationStatus");

  	//gets the geolocation of the user
	if (navigator.geolocation) {
		navigator.geolocation.getCurrentPosition(function (position) {
			var pos = {
 	  			lat: position.coords.latitude,
      			lng: position.coords.longitude
       		};
       		console.log(pos);
       		console.log(position.coords.latitude)
       		console.log(position.coords.longitude)

       	//if successful centres the map on the user and places a marker
		var marker = new google.maps.Marker({position: pos, map: map});
		locationStatusText.innerHTML = "Got location.";
		console.log("Got location");
		latitude = pos.lat;
		longitude = pos.lng;
		});

		var lockLocation = document.createElement("form");
		lockLocation.setAttribute('method', "POST");
		lockLocation.setAttribute('action', '/locklocation');

		var reviewLat = document.createElement("input");
		reviewLat.hidden = true;
		reviewLat.name = "latitude";
		reviewLat.value = latitude;

		var reviewLng = document.createElement("input");
		reviewLng.hidden = true;
		reviewLng.name = "longitude";
		reviewLng.value = longitude;

		var submitButton = document.createElement("input");
		submitButton.type = "submit";
		submitButton.value = "Lock Location";

		lockLocation.appendChild(reviewLat);
		lockLocation.appendChild(reviewLng);
		lockLocation.appendChild(submitButton);

		if (document.getElementById("lockInLocation") != null) {
			document.getElementById("lockInLocation").appendChild(lockLocation);
		}
		

	} else {
		//otherwise prints error
		locationStatusText.innerHTML = "Failed to get location.";
		console.log("Failed to get location");
	}

	//sets the map over the user, or Melbourne if no location found
  var map = new google.maps.Map(
   	document.getElementById('map'), {zoom: 15, center: {lat: longitude, lng:latitude}});

  	//hides all of the aspects of the maps that we don't want
    map.setOptions({styles: styles['hide']})

    //TODO: Hide the stations and show the parks

    //loads all of the locations that have been stored locally
    //and calls the marker that represents the location. The marker
    //locations are then stored in an array

    //https://stackoverflow.com/questions/30012913/google-map-api-v3-add-multiple-infowindows
    var infowindow = new google.maps.InfoWindow({maxWidth: 200});

	for (i = 0; i < locations.length; i++) {

		var content = "<b>"+locations[i].name+"</b>";
	    var image = setIcons(locations[i].icon, smallIcon);
	    var marker = new google.maps.Marker({position: {lat: locations[i].x_coord, lng: locations[i].y_coord }, 
	      	map: map,
	      	icon: image,
	      	contentString: content
	    })
	    marker.data = locations[i];
	    
	    marker.addListener('mouseover', function() {
	    	infowindow.setContent("<div><h3>"+this.data.name+"</h3></div><p>"+this.data.descript+"</p>");
	    	infowindow.open(map, this);
	    })

	    marker.addListener('mouseout', function() {
	    	infowindow.close();
	    })
	    marker.setMap(null);
	    markers.push(marker);
	}

	if (visited == true) {
		for (i = 0; i<visited_locations.length; i++) {
			var marker = new google.maps.Marker({position: {lat: visited_locations[i].x_coord, lng: visited_locations[i].y_coord},
			map: map
			});
			marker.setMap(map)

			console.log(visited_locations[i].x_coord, lng: visited_locations[i].y_coord);
		}
	}

	//Adds a listener to check to see whether the map has been zoomed
	map.addListener('zoom_changed', function() {
		zoom = map.getZoom();

		//Depending on the zoom level, displays the markers, and sets the size
		//of the markers, otherwise hides the markers
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

//Hides the points of interest on the API
var styles = {
  	default: null,
 	hide: [
	{
  		featureType: 'poi',
  		stylers: [{visibility: 'off'}]
  	}]
};

//Functions to set the markers, the icons, and the size of the icons
function setIcons(icon, size) {

	var image = {
	  		url: 'https://storage.googleapis.com/map-icons-cca02/icons/'+icon+'?authuser=2',
	  		scaledSize: new google.maps.Size(size,size),
	  		origin: new google.maps.Point(0,0),
	  		anchor: new google.maps.Point(0,32)
		};
	return image;
}

//Determines whether the icon will be large or small
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