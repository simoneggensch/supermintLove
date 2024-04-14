function formatAuthors(authors) {
    console.log("in format Authors")
    return("hello there");
    var outputString = "";
    for (var i; i < authors.length; i++) {
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

for (quiz in quizzes) {
    console.log(quiz);
}

console.log("js found");