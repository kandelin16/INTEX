function filterGender(drs) {
  input = document.getElementById("filterByGender").value.toLowerCase();
  if (input != "") {
    for (var count = 0; count < drs.length; count++) {
      tempDoc = drs[count];
      genObject = document.getElementById(tempDoc.id + "gender");
      if (genObject.innerHTML.toLowerCase().includes(input)) {
        tempDoc.hidden = false;
      } else {
        tempDoc.hidden = true;
      }
    }
  }
}

function filterState(drs) {
  input = document.getElementById("filterByState").value.toLowerCase();
  passDown = [];
  if (input != "") {
    for (var count = 0; count < drs.length; count++) {
      tempDoc = drs[count];
      genObject = document.getElementById(tempDoc.id + "state");
      if (genObject.innerHTML.toLowerCase().includes(input)) {
        tempDoc.hidden = false;
        passDown.push(tempDoc);
      } else {
        tempDoc.hidden = true;
      }
    }
    filterGender(passDown);
  } else {
    filterGender(drs);
  }
}

function filter() {
  drs = document.getElementsByClassName("drVis");
  input = document.getElementById("filterTable").value.toLowerCase();
  passDown = [];
  if (input != "") {
    for (var count = 0; count < drs.length; count++) {
      tempDoc = drs[count];
      nameObject = document.getElementById(tempDoc.id + "name");
      specObject = document.getElementById(tempDoc.id + "spec");
      credParent = document.getElementById(tempDoc.id + "cred");
      compiledCreds = ""
      
      if (credParent) {
        credObjects = credParent.children;
        for (var i = 0; i < credObjects.length; i++) {
          child = credObjects[i]
          compiledCreds += child.innerHTML
        }
      }

      compiledCreds = compiledCreds.replace(/[.,\/#!$%\^&\*;:{}=\-_`~()]/g,"");
      
      if (nameObject.innerHTML.toLowerCase().includes(input) || specObject.innerHTML.toLowerCase().includes(input) || compiledCreds.toLowerCase().includes(input)) {
        tempDoc.hidden = false;
        passDown.push(tempDoc);
      } 
      else {
        tempDoc.hidden = true;
      }
    }
    
    filterState(passDown);
  } 
  else {
    filterState(drs);
  }
}



function revealtheFORRMMMMMM() {
  if (document.getElementById("thehiddensacredmostholyform").hidden) {
    document.getElementById("thehiddensacredmostholyform").hidden = false;
    document.getElementById("thebuttontorevealthehiddensacredmostholyform").value = "Cancel"
  }
  else {
    document.getElementById("thehiddensacredmostholyform").hidden = true;
    document.getElementById("thebuttontorevealthehiddensacredmostholyform").value = "Add Prescriber"
  }
  
}

function verifyForm() {
  fname = document.getElementById("fname")
  lname = document.getElementById("lname")
  gender = document.getElementById("gender")
  state = document.getElementById("state")
  specialty = document.getElementById("specialty")
  opioid = document.getElementById("opioid")

  if (fname.value != "" && lname.value != "" && gender.value != "" && state.value != "" && specialty.value != "" && opioid.value != "") {
    if (confirm("Would you like to submit the new prescriber?")) {
      document.getElementById("thehiddensacredmostholyform").submit()
    }
  }
  else {
    alert("Please enter all information before submitting.")
  }
}