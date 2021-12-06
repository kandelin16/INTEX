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
    
    //Fix me porfa
    $.ajax({
        url: "updatePrescriber/",
        data: { "drugName": id , "number": element.innerHTML, "npiT": npi},
        type: 'POST'
    })
    
    
    pTag = document.getElementById(id + "P")

    var capInput = document.createElement('span');
    capInput.innerHTML =  pTag.value;
    capInput.setAttribute('id', pTag.id);

    /*replaces the p tag with the input box*/
    pTag.parentNode.replaceChild(capInput, pTag);

    document.getElementById(id).value = "Update"
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