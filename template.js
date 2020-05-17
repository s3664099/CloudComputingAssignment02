var locations = new Array()
var visited = false
var visited_locations = new Array()

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
	locations.push(local);
{% endfor %}

{% if visit_selected == true %}

    console.log("{{visit_selected}}");

    {%for visit in visited_places%}
        x_coord = {{visit.x_coord}}
        y_coord = {{visit.y_coord}}
        visited_places = {"x_coord": x_coord,
                        "y_coord": y_coord
                        };
        visited_locations.push(visited_places);
    {% endfor %}
    visited = true;
{% else %}
    console.log("{{visit_selected}}");
{% endif %}


