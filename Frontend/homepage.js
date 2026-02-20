//this file is for animations and javascript needed for the index.html (main splash page)
import { animate } from 'animejs';

const homePageCreateGameButton =  document.getElementById('homePage_creategame_button');
const homePageJoinGameButtom = document.getElementById('homePage_joingame_button');

const homePageSelectColorLeft = document.getElementById('homepage_ColorLeft');
const homePageSelectColorRight = document.getElementById('homepage_ColorRight');
const homePageSelectTopLeft = document.getElementById('homepage_TopLeft');
const homePageSelectTopRight = document.getElementById('homepage_TopRight');
const homePageSelectBottomLeft = document.getElementById('homepage_BottomLeft');
const homePageSelectBottomRight = document.getElementById('homepage_BottomRight');

const colorArray = ["red", "orange", "yellow", "green", "blue", "purple"];
const topArray = ["top1", "top2", "top3", "top4", "top5"];
const bottomArray = ["bottom1", "bottom2", "bottom3", "bottom4", "bottom5"];



class usersCustomization {
    constructor() {
        this.color = "red";
        this.colorID = 0;
        this.top = "topZero";
        this.topID = 0;
        this.bottom = "BottomZero";
        this.bottomID = 0;
    }

}


//main cards animation, this is just a concept for now
animate('.main-card', {
    opacity: [0, 1],       // animate FROM 0 TO 1
    translateY: [-30, 0],  // slide down from 30px above
    duration: 600,         // in milliseconds
    easing: 'easeOutExpo'  // controls the "feel" of the animation curve
});


currentUser = new usersCustomization();

//button clicks for user customization on homescreen
homePageCreateGameButton.addEventListener('click', function() {requestedGameStart()}); //if homepage start button is pressed call gamestart
//select Color customization
homePageSelectColorLeft.addEventListener('click', function() { currentUser.color = getNewCustomizationInWheel(colorArray, this.colorID, false); });
homePageSelectColorRight.addEventListener('click', function(){currentUser.color = getNewCustomizationInWheel(colorArray, this.colorID, true)});
//select top customization
homePageSelectTopLeft.addEventListener('click', function(){currentUser.top = getNewCustomizationInWheel(topArray, topID, false)});
homePageSelectTopRight.addEventListener('click', function(){currentUser.top = getNewCustomizationInWheel(topArray, topID, true)});
//select bottom customization
homePageSelectBottomLeft.addEventListener('click', function() {currentUser.bottom = getNewCustomizationInWheel(bottomArray, bottomID, false)});
homePageSelectBottomRight.addEventListener('click', function() {currentUser.bottom = getNewCustomizationInWheel(bottomArray, bottomID, true)})











/*
*takes in spot in array and direction and returns a string of the next item wanted, will do tops, bottoms and colors
* @param {string[]} Array the array of the customization piece you would like 
* @param {number} currentID The id number of the matching array type
* @param {boolean} is the array moving right? True if yes, Right if no
**/
function getNewCustomizationInWheel(Array, currentID, isRight){
    if(isRight){
        if(currentID == (Array.length()-1)){
            return Array[0];
        }
        return Array[currentID + 1];
    }else{ // goes left
        if(currentColorID == 0){
            return Array[Array.length()-1]; //return last element
        }
        return Array[currentID - 1];
    }
}





async function requestedGameStart(){
    const url = "WhateverTheFastAPIurlIsToLobby";
    try{
        const response = await fetch(url);
        if(!response.ok){
            throw new error(`http error. status: ${response.status}` );
        }
        const data = await response.json();
        console.log(data);

    }catch(error){
        console.log(error);
        console.log("An Error occured when requesting lobby start.");
    }
    window.location.href = "lobby.html";
    //whatever we need for the game start is done here, like go to lobby screen and do backend stuff
}