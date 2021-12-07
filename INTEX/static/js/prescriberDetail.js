$(document).ready(function(){
    function getCookie(c_name) {
        if(document.cookie.length > 0) {
            c_start = document.cookie.indexOf(c_name + "=");
            if(c_start != -1) {
                c_start = c_start + c_name.length + 1;
                c_end = document.cookie.indexOf(";", c_start);
                if(c_end == -1) c_end = document.cookie.length;
                return unescape(document.cookie.substring(c_start,c_end));
            }
        }
        return "";
    }

    $(function () {
        $.ajaxSetup({
            headers: {
                "X-CSRFToken": getCookie("csrftoken")
            }
        });
    });
});

function changeP(id) {
    pTag = document.getElementById(id + "P")
    /*Creates an input box with the previous value of the p tag*/
    var capInput = document.createElement('input');
    capInput.setAttribute('type', 'number');
    capInput.setAttribute('value', pTag.innerHTML);
    capInput.setAttribute('style', 'width: 60px;')
    capInput.setAttribute('id', pTag.id);

    /*replaces the p tag with the input box*/
    pTag.parentNode.replaceChild(capInput, pTag);

    document.getElementById(id).value = "Save"
}

function submitUpdate(id) {

    element = document.getElementById(id + "P")
    npi = document.getElementById("npi").value
    
    if (confirm("Would you like to update the quantity prescribed?")) {
        //Fix me porfa
        $.ajax({
            url: "../updatePrescriptionCount/",
            data: { "drugName": id , "number": element.value, "npi": npi},
            type: 'POST',
            success: function(data) {
                document.getElementById("totPrecCount").innerHTML = "Total Prescriptions: " + data.newAmount
            },
        })
        
        
        pTag = document.getElementById(id + "P")

        var capInput = document.createElement('span');
        capInput.innerHTML =  pTag.value;
        capInput.setAttribute('id', pTag.id);

        /*replaces the p tag with the input box*/
        pTag.parentNode.replaceChild(capInput, pTag);

        document.getElementById(id).value = "Update"
    }

}

function buttonHandle(id) {
    button = document.getElementById(id)

    if (button.value == "Update") {
        changeP(id)
    }
    else {
        submitUpdate(id)
    }
}

function enableBoxes() {
    inputs = document.getElementsByClassName("updateForm")
    for (var i = 0; i < inputs.length; i++) {
        inputs[i].disabled = false
        document.getElementById("revealAndUpdateButton").value = "Submit"
        document.getElementById("revealAndUpdateButton").selected = false
    }
}

function updateHandler() {
    if (document.getElementById("revealAndUpdateButton").value == "Update Prescriber") {
        enableBoxes()
        document.getElementById("cancelUpdateButton").hidden = false
    }
    else {
        if (confirm("Would you like to update this prescriber?")) {
            document.getElementById("formNo2").submit()
        }
    }
}

function cancelUpdate() {
    inputs = document.getElementsByClassName("updateForm")
    for (var i = 0; i < inputs.length; i++) {
        inputs[i].disabled = true
        document.getElementById("revealAndUpdateButton").value = "Update Prescriber"
        document.getElementById("cancelUpdateButton").hidden = true
    }
}