function filterGender(drs) {
  input = document.getElementById("filterByIsOpioid").value.toLowerCase();
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

function filterDrug() {
  dru = document.getElementsByClassName("drugclass");
  input = document.getElementById("filterTable").value.toLowerCase();
  passDown = [];
  if (input != "") {
    for (var count = 0; count < dru.length; count++) {
      tempDrug = dru[count];

      nameObject = document.getElementById(tempDrug.id + "drugname");
      opioidObject = document.getElementById(tempDrug.id + "isopiod");
      if (
        nameObject.innerHTML.toLowerCase().includes(input) ||
        opioidObject.innerHTML.toLowerCase().includes(input)
      ) {
        tempDrug.hidden = false;
        passDown.push(tempDrug);
      } else {
        tempDrug.hidden = true;
      }
    }
    filterState(passDown);
  } else {
    filterState(dru);
  }
}
