var locations = new Array()

{% for location in location_details %}
    x_coord = {{location.x_coord}};
    y_coord = {{location.y_coord}};
    icon = "{{location.icon}}";
    local = {"x_coord": x_coord,
			"y_coord": y_coord,
			"icon": icon};
	locations.push(local)
{% endfor %}