function displayQuizzes(quizzes) {

    display_str=""
    for ( var i = 0; i< n_quizzes; i++){
        display_str+=displayQuiz(quizzes[i])
    }

    document.getElementById("quizzes").innerHTML = display_str
}


function displayQuiz(quiz) {
     return "<div class='quiz' onclick=showHide(quizLong_" + quiz.quiz_id + ")>" +
        "<div class='quizShort')>" +
            quiz.title + " hosted by " + formatAuthors(quiz.authors) + ": " + quiz.google_slides_url +
            "<div class='dateHosted'>" +
            "Hosted on " + quiz.date_hosted +
        "</div>" +
        "</div>" + 
        "<div class='quizLong hide' id=quizLong_" + quiz.quiz_id +">" +
            createSubtable(quiz) +
        "</div>" +
    "</div>"
}

function createSubtable(quiz) {

    const rounds = quiz.rounds
    const n_topics = rounds.length
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
        returnString += tableCell(rounds[i].name)
    }
    returnString += "</tr>"
    returnString += "<tr>"
    returnString += tableHeaderCell("Category")
    for(var i=0; i < n_topics; i++) {
        returnString += tableCell(createToolTip(rounds[i].description) + rounds[i].topic)
    }
    returnString += "</tr>"
    returnString += "</table>"

    return returnString
}

function openCloseAll() {
    var allQuizzDescriptions = document.getElementsByClassName("quizLong")
    var openQuizzesBtn = document.getElementById("openQuizzesBtn")
    if (areQuizzesOpened) {
        for(var i = 0; i < allQuizzDescriptions.length; i++) {
            allQuizzDescriptions[i].classList.add("hide")
        }
        areQuizzesOpened = false
        openQuizzesBtn.innerHTML="Open All Quizzes"
    } else {
        for(var i = 0; i < allQuizzDescriptions.length; i++) {
            allQuizzDescriptions[i].classList.remove("hide")
        }
        areQuizzesOpened = true
        openQuizzesBtn.innerHTML="Close All Quizzes"

    }
}


function search(searchFieldDiv) {
    console.log(searchFieldDiv.value)
}

