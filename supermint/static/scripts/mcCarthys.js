function displayQuizzes(quizzes) {
    for ( var i = 0; i< n_quizzes; i++){
        document.getElementById("quiz_"+i).innerHTML=displayQuiz(quizzes[i])
    }
}

function displayQuiz(quiz) {
     return quiz['title'] + " created by " +  formatAuthors(quiz['authors']);
}
