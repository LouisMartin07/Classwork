const randomNumber = Math.floor(Math.random() * 100) + 1;

let guessedNumbers = [];

function checkGuess() {
    const userGuess = parseInt(document.getElementById('userGuess').value);

    if (userGuess === randomNumber) {
        showMessage('Congratulations! You guessed the correct number.');
        
    } else {
        guessedNumbers.push(userGuess);

        if (userGuess < randomNumber) {
            showMessage('Try guessing a higher number.');
        } else {
            showMessage('Try guessing a lower number.');
        }
    }
    updateGuessList();
}
function showMessage(message) {
    document.getElementById('message').innerText = message;
}
function updateGuessList() {
    const guessList = document.getElementById('guessList');
    guessList.innerHTML = '<strong>Your Guesses:</strong><br>' + guessedNumbers.join(', ');
}
