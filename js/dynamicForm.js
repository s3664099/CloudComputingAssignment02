
function changeForm() {
    
    document.getElementById("dynamicForm").innerHTML = "";

    var type = document.getElementById("placeType").value;
    var form = document.createElement("form");

    form.setAttribute('method', "POST");
    form.setAttribute('id', "placeForm");
    form.setAttribute('action', '/addplace');

    var formElements = [];

    var placeLabel = document.createElement("label");
    placeLabel.innerHTML = "Place Name: ";
    formElements.push(placeLabel);

    var placeName = document.createElement("input");
    placeName.type = "text";
    placeName.name = "placeName";
    placeName.required = true;
    formElements.push(placeName);

    formElements.push(document.createElement("br"));

    var addressLabel = document.createElement("label");
    addressLabel.innerHTML = "Address: ";
    formElements.push(addressLabel);

    var address = document.createElement("input");
    address.type = "text";
    address.name = "address";
    formElements.push(address);

    formElements.push(document.createElement("br"));

    var townLabel = document.createElement("label");
    townLabel.innerHTML = "Town: ";
    formElements.push(townLabel);

    var town  = document.createElement("input");
    town.type = "text";
    town.name = "town";
    town.required = true;
    formElements.push(town);

    formElements.push(document.createElement("br"));

    var stateLabel = document.createElement("label");
    stateLabel.innerHTML = "State: ";
    formElements.push(stateLabel);

    var state = document.createElement("input");
    state.type = "text";
    state.name = "state";
    state.required = true;
    formElements.push(state);

    formElements.push(document.createElement("br"));

    var countryLabel = document.createElement("label");
    countryLabel.innerHTML = "Country: ";
    formElements.push(countryLabel);

    var country = document.createElement("input");
    country.type = "text";
    country.name = "country";
    country.required = true;
    formElements.push(country);

    formElements.push(document.createElement("br"));

    var emailLabel = document.createElement("label");
    emailLabel.innerHTML = "Email: ";
    formElements.push(emailLabel);

    var email = document.createElement("input");
    email.type = "text";
    email.name = "email";
    formElements.push(email);

    formElements.push(document.createElement("br"));

    var phoneLabel  = document.createElement("label");
    phoneLabel.innerHTML = "Phone Number: ";
    formElements.push(phoneLabel);

    var phone  = document.createElement("input");
    phone.type = "text";
    phone.name = "phone";
    formElements.push(phone);

    formElements.push(document.createElement("br"));

    var webLabel  = document.createElement("label");
    webLabel.innerHTML = "Website: ";
    formElements.push(webLabel);

    var website = document.createElement("input");
    website.type = "text";
    website.name = "website";
    formElements.push(website);

    formElements.push(document.createElement("br"));

    var descLabel  = document.createElement("label");
    descLabel.innerHTML = "Description: ";
    formElements.push(descLabel);

    var description = document.createElement("textarea");
    description.name = "description";
    description.form = "placeForm";
    formElements.push(description);

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
    submitButton.value = "Submit";
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
    placeType.value = "Pub/Bar";
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
    placeType.value = "Cafe";
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
    placeType.value = "Museum";
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
    placeType.value = "Restaurant, Takeaway";
    formElements.push(placeType);

    var valueLabel = document.createElement("label");
    valueLabel.innerHTML = "Value for Money: ";
    formElements.push(valueLabel);

    var valueValues = ["Good", "Bad"];
    addRadioButtonSet(valueValues, formElements, "value");
    formElements.push(document.createElement("br"));  

    var containerLabel = document.createElement("label");
    containerLabel.innerHTML = "Container: ";
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
