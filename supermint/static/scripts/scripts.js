
function formatAuthors(authors) {
    authors = createList(authors)
    console.log("in format Authors with authors " + authors)
    var outputString = "";
    console.log(authors.length)
    for (var i = 0; i < authors.length; i++) {
        console.log(i, " is called ", authors[i])
        outputString += authors[i];
        if (i == authors.length - 2) {
            outputString += " and ";
        } else if (i == authors.length - 1 ) {
            console.log("should return");
            return outputString;
        } else {
            outputString += ", ";
        }
    }
}

function createList(inputString) {
    return inputString.substring(1, inputString.length-1).split(", ")
}
