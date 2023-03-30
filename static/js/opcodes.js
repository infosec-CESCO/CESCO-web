console.log('opcodes.js loaded');

function toggleRow(row, filename) {
    console.log('loadMarkdownFile called with filename:', filename);
    fetch(filename)
        .then(response => response.text())
        .then(md => {
            const mdParser = new markdownit();
            const html = mdParser.render(md);

            const formattedHtml = `<div class="markdown-body">${html}</div>`;

            if (row.getAttribute('data-expanded') === 'true') {
                row.nextSibling.remove();
                row.setAttribute('data-expanded', 'false');
            } else {
                const newRow = document.createElement('tr');
                newRow.classList.add('description');
                const newCell = document.createElement('td');
                newCell.innerHTML = formattedHtml;
                newCell.setAttribute('colspan', row.childElementCount);

                newRow.appendChild(newCell);
                row.parentNode.insertBefore(newRow, row.nextSibling);
                row.setAttribute('data-expanded', 'true');
            }
        });
}

// function changeItem(rowNum) {
//     const btnElement = document.getElementById("language-button");
//     var enDiv = document.getElementById("EN" + rowNum);
//     var krDiv = document.getElementById("KR" + rowNum);
//
//     if (btnElement.innerText == "KR") {
//         btnElement.innerText = "EN";
//         enDiv.style.display = "none";
//         krDiv.style.display = "block";
//     } else {
//         btnElement.innerText = "KR";
//         enDiv.style.display = "block";
//         krDiv.style.display = "none";
//     }
// }







