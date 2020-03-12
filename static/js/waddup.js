console.log('waddup')
// assign form 
let questionForm = document.querySelector('#add-question')

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
        //    body: JSON.stringify({ questionTitle: document.querySelector('#question-title').value, questionBody: document.querySelector('#question-body').value })
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
})


// body: JSON.stringify({ questionTitle: document.querySelector('#question-title').value, questionBody: document.querySelector('#question-body').value  })