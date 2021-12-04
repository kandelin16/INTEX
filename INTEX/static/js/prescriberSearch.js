function filterOpioid(dru) {
  input = document.getElementById("filterIsOpioid").value.toLowerCase();
  if (input != "") {
    for (var count = 0; count < dru.length; count++) {
      tempDrug = dru[count];
      genObject = document.getElementById(tempDoc.id + "isopiod");
      if (genObject.innerHTML.toLowerCase().includes(input)) {
        tempDrug.hidden = false;
      } else {
        tempDrug.hidden = true;
      }
    }
  }
}

function filterDrugName(drs) {
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
      if (
        nameObject.innerHTML.toLowerCase().includes(input) ||
        specObject.innerHTML.toLowerCase().includes(input)
      ) {
        tempDoc.hidden = false;
        passDown.push(tempDoc);
      } else {
        tempDoc.hidden = true;
      }
    }
    filterState(passDown);
  } else {
    filterState(drs);
  }
}
