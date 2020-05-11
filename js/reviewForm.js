function makeReviewForm() {
    document.getElementById("placeForm").innerHTML = "";

    var form = document.createElement("form");

    form.setAttribute('method', "POST");
    form.setAttribute('id', "placeForm");
    form.setAttribute('action', '/review');

    var formElements = [];

    var yesNo = ["Yes", "No"];

    var likeLabel = document.createElement("label");
    likeLabel.innerHTML = "Did you like this location?";
    formElements.push(likeLabel);

    addRadioButtons(yesNo, formElements, "liked");
    formElements.push(document.createElement("br"));

    var reviewLabel = document.createElement("label");
    reviewLabel.innerHTML = "Your Review:";
    formElements.push(reviewLabel);
    formElements.push(document.createElement("br"));

    var reviewText = document.createElement("textarea");
    reviewText.name = "review";
    reviewText.form = "placeForm";
    formElements.push(reviewText);
    formElements.push(document.createElement("br"));
    
    var submitButton = document.createElement("input");
    submitButton.type = "submit";
    submitButton.value = "Submit Review";
    formElements.push(submitButton);

    for (element of formElements) {
        form.appendChild(element);
    }


    document.getElementById('placeForm').appendChild(form)
}

function addRadioButtons(values, formElements, fieldName) {
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