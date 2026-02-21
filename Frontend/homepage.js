// GRAB ELEMENTS FROM THE DOM 
//if adding anything, put it here
const nameInput        = document.getElementById('name-input');
const figureHead       = document.getElementById('figure-head');
const figureBody       = document.getElementById('figure-body');
const figureNameBadge  = document.getElementById('figure-name-badge');
const swatches         = document.querySelectorAll('.swatch'); // gets ALL elements with class "swatch"
const createGameButton = document.getElementById('create-game-button');
const joinGameButton   = document.getElementById('join-game-button');
const gameCodeInput    = document.getElementById('game-code-input');


// ================================
// PLAYER STATE
// We track what the player has selected here.
// This is what eventually gets sent to the backend.
// ================================
let playerState = {
    name: '',
    color: 'GRAY',
};


// ================================
// NAME INPUT — live preview
// 'input' fires every time the user types a character.
// ================================
nameInput.addEventListener('input', function() {
    playerState.name = nameInput.value;

    // Update the badge under the figure in real time.
    // If the field is empty, show "???" as a placeholder.
    if (nameInput.value.trim() === '') {
        figureNameBadge.textContent = '???';
    } else {
        figureNameBadge.textContent = nameInput.value.toUpperCase();
    }
});


// ================================
// COLOR SWATCHES — live preview
//
// We loop over every swatch and attach a click listener.
// When one is clicked:
//   1. We remove "selected" from all swatches
//   2. We add "selected" to the one that was clicked
//   3. We read its data-color attribute to know which color was picked
//   4. We update the figure's color
// ================================
swatches.forEach(function(swatch) {
    swatch.addEventListener('click', function() {

        // Step 1: clear selection from everything
        swatches.forEach(function(s) { s.classList.remove('selected'); });

        // Step 2: mark this one as selected
        swatch.classList.add('selected');

        // Step 3: read the color name (e.g. "GREEN", "RED")
        const pickedColor = swatch.dataset.color;  // reads the data-color attribute
        playerState.color = pickedColor;

        // Step 4: update the figure — we grab the actual CSS color from the swatch's background
        // getComputedStyle reads the actual rendered color of the element
        const actualCSSColor = getComputedStyle(swatch).backgroundColor;
        figureHead.style.backgroundColor = actualCSSColor;
        figureBody.style.backgroundColor = actualCSSColor;
    });
});


// ================================
// CREATE GAME BUTTON
// For now: just redirect to lobby.html.
// Later: send playerState to backend first, then redirect.
// ================================
createGameButton.addEventListener('click', function() {
    // TODO: validate that name is not empty before allowing this
    window.location.href = 'lobby.html';
});


// ================================
// JOIN GAME BUTTON
// For now: just logs what would be sent.
// Later: send playerState + game code to backend.
// ================================
joinGameButton.addEventListener('click', function() {
    const code = gameCodeInput.value.trim().toUpperCase();

    if (code.length !== 5) {
        alert('Game code must be 5 characters!');
        return;
    }

    // TODO: send playerState and code to backend
    console.log('Joining game with:', playerState, 'Code:', code);
});