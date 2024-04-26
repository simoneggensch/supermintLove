function displayQuizzes(quizzes) {

    display_str=""
    for ( var i = 0; i< n_quizzes; i++){
        display_str+=displayQuiz(quizzes[i])
    }

    document.getElementById("quizzes").innerHTML = display_str
}


function displayQuiz(quiz) {
     return "<div class='quiz'>" +
        "<div class='quizShort'>" +
            quiz.title + " hosted by " + formatAuthors(quiz.authors) + ": " + quiz.google_slides_url +
        "</div>" + 
        "<div class='dateHosted'>" +
            "Hosted on " + quiz.date_hosted +
        "</div>" +
        "<div class='quizLong'>" +
            createSubtable(quiz) +
        "</div>" +
    "</div>"
}

function createSubtable(quiz) {

    const titles = createList(quiz.round_titles)
    const topics = createList(quiz.round_topics)
    const n_topics = titles.length
    returnString = "<table>"
    returnString += "<tr>"
    returnString += tableHeaderCell("")
    for(var i=0; i < n_topics; i++) {
        returnString += tableHeaderCell("Round " + (i+1))
    }
    returnString += "</tr>"
    returnString += "<tr>"
    returnString += tableHeaderCell("Title")
    for(var i=0; i < n_topics; i++) {
        returnString += tableHeaderCell(titles[i])
    }
    returnString += "</tr>"
    returnString += "<tr>"
    returnString += tableHeaderCell("Category")
    for(var i=0; i < n_topics; i++) {
        returnString += tableHeaderCell(topics[i])
    }
    returnString += "</tr>"
    returnString += "</table>"

    return returnString
}
