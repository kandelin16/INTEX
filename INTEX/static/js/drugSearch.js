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
