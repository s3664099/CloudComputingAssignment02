var locations = new Array()
var visited = false
var visited_locations = new Array()
var v_buttons = new Array()

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
    view_button = "<form action = '\View_Place' method = 'post'><input name = 'co_ords' value = '{{location.x_coord}},{{location.y_coord}}'></form>";
    v_buttons.push(view_button);
{% endfor %}

{% if visit_selected == true %}

    {%for visit in visited_places%}
        console.log("{{visit.x_coord}}","{{visit.y_coord}}")
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


