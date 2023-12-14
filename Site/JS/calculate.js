const form = document.querySelector(".form");

async function postData(url = '', data){

    const respone = await fetch(url, {
        method: "POST",
        mode: "cors",
        headers: {
            "Content-Type": "application/json",
        },
        body: JSON.stringify(data)
    });

    return respone.json()
}

form.addEventListener("submit", e => {

    answerjson = {
        
    };

    e.preventDefault();
    children = [...e.target.children]
    children.forEach(e => {

        if(e.children[1] !== undefined){

            answerArray.push(e.children[1].value); 
        }
    });
    console.log(answerArray)
    console.log(JSON.stringify(answerArray))
    postData("http://localhost:8000/calculated", JSON.stringify(answerArray)).then(e => console.log(e));

});
