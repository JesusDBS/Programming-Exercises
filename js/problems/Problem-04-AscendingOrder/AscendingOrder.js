/*Ascending order:

Create a program that, given 4 values A, B, C, D, 
displays them on the screen, ordered from smallest to largest.*/

let numbers = [];

while(true){
    let number = Number(prompt("Insert a number: "));
    numbers.push(number);
  
    numbers = new Set(numbers);
    numbers = Array.from(numbers);

    if(numbers.length >= 4){
        alert(numbers.sort());
        break;
    }
}

