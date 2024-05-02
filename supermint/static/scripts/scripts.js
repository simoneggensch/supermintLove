
function formatAuthors(authors) {
    var outputString = "";
    for (var i = 0; i < authors.length; i++) {
        outputString += authors[i];
        if (i == authors.length - 2) {
            outputString += " and ";
        } else if (i == authors.length - 1 ) {
            return outputString;
        } else {
            outputString += ", ";
        }
    }
}

function createList(inputString) {
    return inputString.substring(1, inputString.length-1).split(", ")
}

function tableHeaderCell(content) {
    return "<th>" + content + "</th>"
}

function tableRow(content) {
    return "<tr>" + content + "</tr>"
}

function tableCell(content) {
    return "<td>" + content + "</td>"
}

function showHide(div) {
    if(div.classList.contains("hide")) {
        div.classList.remove("hide")
    } else {
        div.classList.add("hide")
    }
}


function createToolTip(innerText) {
    return "<span class='quizDescription'>" + innerText + "</span>"
}