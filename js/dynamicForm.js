
function changeForm() {
    
    document.getElementById("dynamicForm").innerHTML = "";

    var type = document.getElementById("placeType").value;
    var form = document.createElement("form");

    form.setAttribute('method', "POST");
    form.setAttribute('id', "reviewForm");
    form.setAttribute('action', '/review');

    var formElements = [];

    var reviewLat = document.createElement("input");
    reviewLat.hidden = true;
    reviewLat.name = "latitude";
    reviewLat.value = "";
    formElements.push(reviewLat);

    var reviewLng = document.createElement("input");
    reviewLng.hidden = true;
    reviewLng.name = "longitude";
    reviewLng.value = "";
    formElements.push(reviewLng);

    if (navigator.geolocation) {
        navigator.geolocation.getCurrentPosition(function (position) {
			var pos = {
 	  			lat: position.coords.latitude,
      			lng: position.coords.longitude
       		};
		reviewLat.value = pos.lat;
		reviewLng.value = pos.lng;
		});
    }

    var yesNo = ["Yes", "No"];

    var likeLabel = document.createElement("label");
    likeLabel.innerHTML = "Did you like this location?";
    formElements.push(likeLabel);

    addRadioButtonSet(yesNo, formElements, "liked");
    formElements.push(document.createElement("br"));

    var reviewLabel = document.createElement("label");
    reviewLabel.innerHTML = "Your Review:";
    formElements.push(reviewLabel);
    formElements.push(document.createElement("br"));

    var reviewText = document.createElement("textarea");
    reviewText.name = "review";
    reviewText.form = "reviewForm";
    formElements.push(reviewText);
    formElements.push(document.createElement("br"));

    if (type == "bar") {
        makeBarForm(formElements);
    }

    if (type == "cafe") {
        makeCafeForm(formElements);
    }

    if (type == "museum") {
        makeMuseumForm(formElements);
    }

    if (type == "takeaway") {
        makeTakeawayForm(formElements);
    }

    var submitButton = document.createElement("input");
    submitButton.type = "submit";
    submitButton.value = "Submit Review";
    formElements.push(submitButton);

    for (element of formElements) {
        form.appendChild(element);
    }


    document.getElementById('dynamicForm').appendChild(form);
}

function makeBarForm(formElements) {
    var placeType = document.createElement("input");
    placeType.hidden = true;
    placeType.name = "type";
    placeType.value = "bar";
    formElements.push(placeType);

    var craftLabel = document.createElement("label");
    craftLabel.innerHTML = "Craft Beer Rating:";
    formElements.push(craftLabel);

    var craftRatings = ["Good", "Okay", "None"]

    addRadioButtonSet(craftRatings, formElements, "craftBeer");
    formElements.push(document.createElement("br"));

    var gardenLabel = document.createElement("label");
    gardenLabel.innerHTML = "Beer Garden:";
    formElements.push(gardenLabel);

    var yesNo = ["Yes", "No"];

    addRadioButtonSet(yesNo, formElements, "beerGarden");
    formElements.push(document.createElement("br"));
    
    var roofLabel = document.createElement("label");
    roofLabel.innerHTML = "Rooftop Deck:";
    formElements.push(roofLabel);

    addRadioButtonSet(yesNo, formElements, "rooftopDeck");
    formElements.push(document.createElement("br"));

    var pokieLabel = document.createElement("label");
    pokieLabel.innerHTML = "Poker Machines:";
    formElements.push(pokieLabel);

    var pokieRatings = ["Lots", "Few", "None"];

    addRadioButtonSet(pokieRatings, formElements, "pokies");
    formElements.push(document.createElement("br"));

    var sportsBarLabel = document.createElement("label");
    sportsBarLabel.innerHTML = "Sports Bar:";
    formElements.push(sportsBarLabel);

    addRadioButtonSet(yesNo, formElements, "sportsBar");
    formElements.push(document.createElement("br"));

    var atmosLabel = document.createElement("label");
    atmosLabel.innerHTML = "Atmosphere:";
    formElements.push(atmosLabel);

    var atmosValues = ["Tacky", "Grungy", "Hip", "Trendy"];

    addRadioButtonSet(atmosValues, formElements, "atmosphere");
    formElements.push(document.createElement("br"));

    var animalPermitLabel = document.createElement("label");
    animalPermitLabel.innerHTML = "Animal Permitted:";
    formElements.push(animalPermitLabel);

    addRadioButtonSet(yesNo, formElements, "animalPermitted");
    formElements.push(document.createElement("br"));
}

function makeCafeForm(formElements) {
    var placeType = document.createElement("input");
    placeType.hidden = true;
    placeType.name = "type";
    placeType.value = "cafe";
    formElements.push(placeType);

    var coffeeLabel = document.createElement("label");
    coffeeLabel.innerHTML = "Coffee Rating:";
    formElements.push(coffeeLabel);

    var coffeeValues = ["Good", "Okay", "Bad"];
    addRadioButtonSet(coffeeValues, formElements, "coffee");
    formElements.push(document.createElement("br"));

    var teaLabel = document.createElement("label");
    teaLabel.innerHTML = "Tea Rating:";
    formElements.push(teaLabel);

    var teaValues = ["Strong", "Good", "Bad"];
    addRadioButtonSet(teaValues, formElements, "tea");
    formElements.push(document.createElement("br"));

    var teaPotLabel = document.createElement("label");
    teaPotLabel.innerHTML = "Tea Pot:";
    formElements.push(teaPotLabel);

    var teaPotValues = ["Big", "Small", "Cup"];
    addRadioButtonSet(teaPotValues, formElements, "teaPot");
    formElements.push(document.createElement("br"));

    var sugarLabel = document.createElement("label");
    sugarLabel.innerHTML = "Sugar:";
    formElements.push(sugarLabel);

    var sugarValues = ["Good", "Bad"];
    addRadioButtonSet(sugarValues, formElements, "sugar");
    formElements.push(document.createElement("br"));

    var keepLabel = document.createElement("label");
    keepLabel.innerHTML = "Keep Cup Discount:";
    formElements.push(keepLabel);

    var keepValues = ["Yes", "No"];
    addRadioButtonSet(keepValues, formElements, "keepCupDiscount");
    formElements.push(document.createElement("br"));
}

function makeMuseumForm(formElements) {
    var placeType = document.createElement("input");
    placeType.hidden = true;
    placeType.name = "type";
    placeType.value = "museum";
    formElements.push(placeType);

    var entryLabel = document.createElement("label");
    entryLabel.innerHTML = "Entry Fee:";
    formElements.push(entryLabel);

    var entryValues = ["Free", "Cheap", "Pricey"];
    addRadioButtonSet(entryValues, formElements, "entryFee");
    formElements.push(document.createElement("br"));  

    var timeLabel = document.createElement("label");
    timeLabel.innerHTML = "Time Allowed:";
    formElements.push(timeLabel);

    var timeValues = ["Short", "Medium", "Long"];
    addRadioButtonSet(timeValues, formElements, "timeAllowed");
    formElements.push(document.createElement("br"));
}

function makeTakeawayForm(formElements) {
    var placeType = document.createElement("input");
    placeType.hidden = true;
    placeType.name = "type";
    placeType.value = "takeaway";
    formElements.push(placeType);

    var valueLabel = document.createElement("label");
    valueLabel.innerHTML = "Value for Money:";
    formElements.push(valueLabel);

    var valueValues = ["Good", "Bad"];
    addRadioButtonSet(valueValues, formElements, "value");
    formElements.push(document.createElement("br"));  

    var containerLabel = document.createElement("label");
    containerLabel.innerHTML = "Container";
    formElements.push(containerLabel);

    var containerValues = ["Styrofoam", "Cardboard", "Plastic"];
    addRadioButtonSet(containerValues, formElements, "containers");
    formElements.push(document.createElement("br"));
}

function addRadioButtonSet(values, formElements, fieldName) {
    for (value of values) {
        var radio = document.createElement("input");
        radio.type = "radio";
        radio.name = fieldName;
        radio.value = value;
        radio.id = fieldName + value;
        radio.required = true;
        console.log(radio.id);
        formElements.push(radio);
        var label = document.createElement("label");
        label.setAttribute("for", fieldName + value);
        label.innerHTML = value;  
        formElements.push(label); 
    }       
}
