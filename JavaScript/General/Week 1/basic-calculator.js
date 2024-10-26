

// const operation = (a, b, operation) => {
//   switch (operation) {
//     case '+':
//       return a + b;
//     case '-':
//       return a - b;
//     case '*':
//       return a * b;
//     case '/':
//       return a / b;
//     default:
//       break;
//   }
// }


// console.log(operation('3', '5', '-'));

// function guessingGame() {
//   let randomNumber = Math.floor(Math.random() * 100) + 1;
//   let isGameOver = false;

//   console.log("I'm thinking of a number between 1 and 100. Can you guess it?");

//   while (!isGameOver) {

//     if (guess === randomNumber) {
//       console.log("Congratulations! You guessed it correctly.");
//       isGameOver = true;
//     } else if (guess < randomNumber) {
//       console.log("Too low. Try again.");
//     } else {
//       console.log("Too high. Try again.");
//     }
//   }
// }

// guessingGame();


// console.log("hello world");

const operation = '12 + 9 * 3 - 12 / 3';

let newOperation = operation.split(" ");
console.log(newOperation);

let currentNumber = 0;
let nextNumber = 0;
let indexOfNextNumber = 2;


for (num of newOperation) {

  if (parseInt(num)) {

    let newInt = parseInt(num)
    if (parseInt(newOperation[indexOfNextNumber])) nextNumber = parseInt(newOperation[indexOfNextNumber]);

    if (indexOfNextNumber == 2) {
      currentNumber += newInt;
    }
    indexOfNextNumber += 2;
  } else {
    if (num == '+') {
      currentNumber += nextNumber;
    } else if (num == '-') {
      currentNumber = currentNumber -= nextNumber;
    } else if (num == '*') {
      currentNumber = currentNumber *= nextNumber;
    } else if (num == '/') {
      currentNumber = currentNumber /= nextNumber;
    }
  }

}

let result = currentNumber;
console.log('this is the result', result,);


//  function calculator(operation) {
//   let newOperation = operation.split('');
//   console.log(newOperation);
//   for(i of newOperation) {
//       const op = i;
//       if (i=='+' || i=='-' || i=='*'||i=='/') {
//         console.log('operator');
//         console.log(i);
//       } else {
//          var intergervalues = parseInt(i);
//         console.log(typeof(intergervalues));
//         console.log(intergervalues);
//       }
//   }
// }


// console.log(calculator('1+2-3'))







const bodmasCalculator = (operation) => {
  let newOpr = operation.split(" ");
  let result = 0;
  for(i of newOpr) {
    if(i == "+") {
      
    } else if(i == "-") {

    } else if(i == "*") {
      
    } else if(i == "/") {

    }
  }
}


bodmasCalculator('12 + 9 * 3 - 12 / 3')