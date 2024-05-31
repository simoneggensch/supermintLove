function additionalAuthor(users) {
    var select = document.createElement("select")
    select.classList.add("author")
    formatUserSelect(select, users)
    listOfAuthors.append(select)
}

function formatUserSelect(selectElem, users) {
    var innerHTML = "";
    for (user of users) {
        var option = document.createElement("option");
        option.innerHTML = getUniqueName(user.id, users)
        option.value = user.id
        selectElem.add(option)
    } 
}

function getUniqueName(userId, users) {
    var user = users.filter(u => u.id == userId)[0];
    var usersWithSameName = users.filter(u => u.first_name == user.first_name);
    if ( usersWithSameName.length == 1) {
        return user.first_name;
    } else {
        return user.first_name + ' ' + user.last_name;
    }
}

function removeLastAuthor() {
    var authors = document.getElementsByClassName("author")
    authors[authors.length-1].parentNode.removeChild(authors[authors.length-1])
}


function showHideAddNewUser() {

    if(addNewUser.classList.contains("hide")) {
        showHideNewUserButton.innerHTML="Hide New User Window"    
    } else {
        showHideNewUserButton.innerHTML="Add New User"
    }
    showHide(addNewUser);
}

function showHideAddNewTopic() {

    if(addNewTopic.classList.contains("hide")) {
        showHideNewTopicButton.innerHTML="Hide New Topic Window"    
    } else {
        showHideNewTopicButton.innerHTML="Add New Topic"
    }
    showHide(addNewTopic);
}

function additionalRound(users) {
    var roundForm = createRoundForm();
    listOfRounds.append(roundForm)
}

function createRoundForm() {
    var div = document.createElement("div")
    div.id="round_" + (listOfRounds.children.length + 1)
    div.classList.add("round")

    div.appendChild(addInDiv(createRoundTitle()))
    div.appendChild(addInDiv(createRoundTopic()))
    div.appendChild(addInDiv(createRoundDescription()))

    return div
}

function createRoundTitle() {
    var title = document.createElement("input")
    title.name = "name"
    return title
}

function createRoundTopic() {
    var select = document.createElement("select")
    select.name = "topic"
    for (topic of topics) {
        var option = document.createElement("option");
        option.innerHTML = topic.name
        option.value = topic.id
        select.add(option)
    }
    return select
}

function createRoundDescription() {
    var description = document.createElement("input")
    description.name = "description"
    description.classList.add("roundDescription")
    return description
}

function removeLastRound() {
    var rounds = document.getElementsByClassName("round")
    rounds[rounds.length-1].parentNode.removeChild(rounds[rounds.length-1])
}

function submitNewUser() {
    const formData = getNewUserData()
    submitDataAndReload(formData, "/submit/user")
}

function getNewUserData() {
    const formData = new FormData
    paragraphs = document.getElementById("addNewUser").children;
    for (var i = 0; i< paragraphs.length - 1; i++) {
        var input = paragraphs[i].getElementsByTagName("input")[0]
        formData.append(input.name, input.value)
    }
    return formData
}

function submitNewTopic() {
    const formData = getNewTopicData()
    submitDataAndReload(formData, "/submit/topic")
}

function getNewTopicData() {
    const formData = new FormData
    topicElem = document.getElementById("addNewTopic").children[0];
    input = topicElem.getElementsByTagName("input")[0]
    formData.append(input.name, input.value)
    return formData
}

function submitNewQuiz() {
    const formData = getNewQuizData()
    submitDataAndReload(formData, "/submit/quiz")
}

function getNewQuizData() {
    const formData = new FormData
    formData.append("quizTitle", getValueFromInputField(quizTitleInput, "Quiz Title"))
    formData.append("authors", getAuthors())
    formData.append("rounds", getRounds())
    formData.append("locationId", getValueFromInputField(quizLocation, "Location"))
    formData.append("googleDriveLink", getValueFromInputField(googleDriveURLInput, "Google Drive URL"))
    formData.append("hostDate", getValueFromInputField(hostDateInput, "Date of Hosting"))
    return formData
}

function getAuthors() {
    authors = []
    authorElems = listOfAuthors.children
    for (let authorElem of authorElems) {
        authors = authors.concat([authorElem.value])
    }
    return authors
}

function getRounds() {
    rounds = []
    for (let roundElem of listOfRounds.children) {
        var round = {}
        for (let divElem of roundElem.children) {
            let elem = divElem.children[0]
            round[elem.name] = getValueFromInputField(elem, elem.name + " for round " + (rounds.length + 1), elem.name = 'quizLocation')
        }
        rounds = rounds.concat([round])
    }
    return JSON.stringify(rounds)
}

function getValueFromInputField(inputField, fieldName = "a value", allowEmpty=false) {
    const value = inputField.value
    if (!allowEmpty && value == '') {
        const errorText = fieldName + ' is missing'
        alert(errorText)
        throw Error(fieldName + ' is missing')
    }
    return value
}

function submitDataAndReload(data, route) {
    fetch(route, {
        method: 'POST',
        body: data
    })
    .then(() => location.reload())
}
