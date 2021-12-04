function filterOpioid(drus) {
  input = document.getElementById("filterIsOpioid").value.toLowerCase();
  if (input != "") {
    for (var count = 0; count < drus.length; count++) {
      tempDru = drus[count];
      opObject = document.getElementById(tempDru.id + "isopiod");
      if (opObject.innerHTML.toLowerCase().includes(input)) {
        tempDru.hidden = false;
      } else {
        tempDru.hidden = true;
      }
    }
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
      if (
        nameObject.innerHTML.toLowerCase().includes(input)
      ) {
        tempDrug.hidden = false;
        passDown.push(tempDrug);
      } else {
        tempDrug.hidden = true;
      }
    }
    filterOpioid(passDown);
  } else {
    filterOpioid(dru);
  }
}
