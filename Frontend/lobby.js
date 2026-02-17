//this file is to handle what will happen inside of the lobby




const inLobbyStartGameButton = document.getElementById('startGame_button');


inLobbyStartGameButton.addEventListener('click', function(){gameMustStart()});






async function gameMustStart(){
    const url = "WhateverTheFastAPIurlIsToGamePage";
    try{
        const response = await fetch(url);
        if(!response.ok){
            throw new error(`http error. status: ${response.status}` );
        }
        const data = await response.json();
        console.log(data);

    }catch(error){
        console.log(error);
        console.log("An Error occured when requesting game start.");
    }
    window.location.href = "gamepage.html";
}
