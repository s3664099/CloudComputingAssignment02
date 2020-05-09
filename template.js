var locations = new Array()

{% for location in location_details %}

    x_coord = {{location.x_coord}};
    y_coord = {{location.y_coord}};
    rating = {{location.rating}};
    icon = "{{location.icon}}";
    name = "{{location.name}}";
    descript = "{{location.description}}";
    local = {"x_coord": x_coord,
			"y_coord": y_coord,
			"rating": rating,
			"icon": icon,
			"name": name,
			"descript": descript};
	locations.push(local)
{% endfor %}
