function toggleRow(rowNum) {
    var row = document.getElementById("row" + rowNum);
    if (row.style.display === "none") {
        row.style.display = "table-row";
    } else {
        row.style.display = "none";
    }
}

function changeItem(rowNum) {
    const btnElement = document.getElementById("language-button");
    var enDiv = document.getElementById("EN" + rowNum);
    var krDiv = document.getElementById("KR" + rowNum);

    if (btnElement.innerText == "KR") {
        btnElement.innerText = "EN";
        enDiv.style.display = "none";
        krDiv.style.display = "block";
    } else {
        btnElement.innerText = "KR";
        enDiv.style.display = "block";
        krDiv.style.display = "none";
    }
}