//this file is for animations and javascript needed for the index.html (main splash page)

const homePageCreateGameButton =  document.getElementById('homePage_creategame_button');


homePageCreateGameButton.addEventListener('click', function() {requestedGameStart()}) //if homepage start button is pressed call gamestart











async function requestedGameStart(){
    const url = "WhateverTheFastAPIurlIs";
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
    window.location.href = "lobby.html";
    //whatever we need for the game start is done here, like go to lobby screen and do backend stuff
}