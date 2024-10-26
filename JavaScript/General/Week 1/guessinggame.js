console.log('Hello world, this works');
alert('You have 5 trials at this game! play wisely😉');

let guessField = document.querySelector('.guess-field');
let randomNumberField = document.querySelector('.random-number-field');
let randomNumberFieldLabel = document.querySelector('.random-number-field-label');
let guessButton = document.querySelector('#guess-button');
let fieldContainer = document.querySelector('.field-container');

let guessCount = 0;

const generateGuess = () => {
  let randomNumber = Math.floor(Math.random() * 10);
  let guess = parseInt(guessField.value);
 


  if (guessCount < 5) {
    let newGuessCount = guessCount + 1;
    guessCount = newGuessCount;
    console.log('current guess count', guessCount)
    if (!parseInt(guess)) alert('Please enter an integer');
    if (parseInt(guess) < 0) {
      alert('Please enter a positive integer');
      return;
    };
    if (parseInt(guess) > 6) {
      alert('Your guess should not be above 10')
      return;
    };

    randomNumberField.innerText = randomNumber;
    if (randomNumber == guess) {
      randomNumberFieldLabel.innerText = 'Great! You got it right👍😉';
      guessCount = 0;
      fieldContainer.style.background = '#a6e7a9';
      randomNumberFieldLabel.style.color = 'green';
      randomNumberField.style.color = 'green';
    } else {
      randomNumberFieldLabel.innerText = 'Awwwn! You got it wrong🥲🥲';
      fieldContainer.style.background = '#f7baba';
      randomNumberFieldLabel.style.color = 'red';
      randomNumberField.style.color = 'red';
    }
  } else {
    alert("Ooops, you've run out of chances🥲.")
    window.location.reload();
  }
}


guessButton.addEventListener("click", generateGuess);