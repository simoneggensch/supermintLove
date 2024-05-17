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
        selectElem.add(option)
    } 
}

function getUniqueName(userId, users) {
    console.log("In get Unique Name")
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
        showHideNewUserButton.innerHTML="Hide New User Option"    
    } else {
        showHideNewUserButton.innerHTML="Add New User"
    }
    showHide(addNewUser);
}


function additionalRound(users) {
    var roundForm = createRoundForm();
    listOfRounds.append(roundForm)
}

function createRoundForm() {
    var div = document.createElement("div")
    div.id="round_" + listOfRounds.length + 1
    div.classList.add("round")

    div.appendChild(addInDiv(createRoundTitle()))
    div.appendChild(addInDiv(createRoundTopic()))
    div.appendChild(addInDiv(createRoundDescription()))

    return div
}

function createRoundTitle() {
    var input = document.createElement("input")
    return input
}

function createRoundTopic() {

    var select = document.createElement("select")

    for (topic of topics) {
        var option = document.createElement("option");
        option.innerHTML = topic.name
        select.add(option)
    }
    return select
}

function createRoundDescription() {
    var description = document.createElement("input")
    description.classList.add("roundDescription")
    return description
}

function removeLastRound() {
    var rounds = document.getElementsByClassName("round")
    rounds[rounds.length-1].parentNode.removeChild(rounds[rounds.length-1])
}