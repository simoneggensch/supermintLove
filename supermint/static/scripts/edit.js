function loadQuizzes() {
    $.ajax({
        url: "/edit/quiz",
        type: 'GET',
        contentType: false,
        success: function(response) {
            console.log(response)
        }
    })
}



function additionalAuthor() {
    var select = document.createElement("select")
    select.classList.add("author")
    formatUserSelect(select)
    listOfAuthors.append(select)
}

function formatUserSelect(selectElem) {
    var innerHTML = "";
    for (user of users) {
        addUsersToSelector(selectElem, user)
    } 
}

function addUsersToSelector(selectElem, user) {
    var option = document.createElement("option");
    option.innerHTML = getUniqueName(user.id)
    option.value = user.id
    selectElem.add(option)
}

function getUniqueName(userId) {
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

function additionalRound() {
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
    title.placeholder="Round Title"
    return title
}

function createRoundTopic() {
    var select = document.createElement("select")
    select.name = "topic"
    select.classList.add("topic")
    addOptionsToTopicsSelect(select)
    return select
}

function addOptionsToTopicsSelect(selectElem) {
    for (topic of topics) {
        var option = document.createElement("option");
        option.innerHTML = topic.name
        option.value = topic.id
        selectElem.add(option)
    }
}

function createRoundDescription() {
    var description = document.createElement("input")
    description.name = "description"
    description.classList.add("roundDescription")
    description.placeholder="Optional Longer Description"
    return description
}

function removeLastRound() {
    var rounds = document.getElementsByClassName("round")
    rounds[rounds.length-1].parentNode.removeChild(rounds[rounds.length-1])
}

function submitNewUser() {
    const formData = getNewUserData();
    $.ajax({
        url: "/submit/user",
        type: 'POST',
        data: formData,
        processData: false,
        contentType: false,
        success: function(response) {
            alert("New User Added with name " + formData.get("firstName") + " " + formData.get("lastName"))
            users = response
            showHideAddNewUser()
            updateAuthorSelectors()
        }
    });
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

function addNewUserToPage(newUser) {
    for (selectElem of listOfAuthors.children) {
        addUsersToSelector(selectElem, newUser)
    }
}


function updateAuthorSelectors() {
    selectedAuthors = []
    while (listOfAuthors.children.length != 0) {
        selectedAuthors.push(listOfAuthors.children[listOfAuthors.children.length-1].value)
        removeLastAuthor()
    }

    while (selectedAuthors.length != 0) {
        additionalAuthor()
        listOfAuthors.children[listOfAuthors.children.length-1].value = selectedAuthors.pop()
    }
}

function submitNewTopic() {
    const formData = getNewTopicData()

    $.ajax({
        url: "/submit/topic",
        type: 'POST',
        data: formData,
        processData: false,
        contentType: false,
        success: function(response) {
            alert("New Topic added: " + formData.get("topicName"))
            topics = response
            updateTopicSelectors()
            showHideAddNewTopic()
        }
    });
}

function getNewTopicData() {
    const formData = new FormData
    topicElem = document.getElementById("addNewTopic").children[0];
    input = topicElem.getElementsByTagName("input")[0]
    formData.append(input.name, input.value)
    return formData
}

function updateTopicSelectors() {
    for (selectElem of document.getElementsByClassName("topic")) {
        const currVal = selectElem.value
        emptySelect(selectElem)
        addOptionsToTopicsSelect(selectElem)
        selectElem.value = currVal
    }
}

function emptySelect(selectElem) {
    while (selectElem.options.length > 0) {
        selectElem.remove(0)
    }
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
