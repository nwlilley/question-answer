console.log('waddup')
// assign form 
let questionForm = document.querySelector('#add-question')

function createQuestionHTML (data) {
    return `<p>${data.title} ${data.body}</p>`
}

function showQuestion (data) {
    const questionHTML = createQuestionHTML(data)
    const questionContainer = document.querySelector("#question-container")
    questionContainer.insertAdjacentHTML('beforeend', questionHTML)
}

function askQuestion() {
    // const questionButton = document.querySelector('#question-submit')
    questionForm.addEventListener("submit", function(e){
        e.preventDefault()
        let questionTitle = document.querySelector("#question-title")
        let questionBody = document.querySelector("#question-body")
        let data = {title: questionTitle.value, body: questionBody.value }
        
        console.log('button connected')
        console.log(data)
        fetch('/newquestion/', {
            method: 'POST',
            headers: {'Content-type': 'application/json',},
            body: JSON.stringify(data)
        })

            .then(res => res.json())
            .then(json => {
                if (json.status === 'ok'){
                    showQuestion(json.data)
                    console.log('GOOD JOB')
                }
            })
    })
}

let answerForm = document.querySelector('#add-answer')

function answerQuestion() {
    answerForm.addEventListener("submit", function(e){
        e.preventDefault()

        console.log('button connected')

        let answer = document.querySelector("#answer-body")
       
        let data = {answer: answer.value}
        
        
        console.log(data)
        fetch('/answer/', {
            method: 'POST',
            headers: {'Content-type': 'application/json',},
            body: JSON.stringify(data)
        })

            .then(res => res.json())
            .then(json => {
                if (json.status === 'ok'){
                    console.log('GOOD JOB')
                }
            })
    })
}

document.addEventListener('DOMContentLoaded', function() {
    askQuestion()
    answerQuestion()
})



// body: JSON.stringify({ questionTitle: document.querySelector('#question-title').value, questionBody: document.querySelector('#question-body').value  })