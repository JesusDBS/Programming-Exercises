/* Average:

In this exercise you will create a program that computes the average of a collection
of values entered by the user. The user will enter 0 as a sentinel value to indicate
that no further values will be provided. Your program should display an appropriate
error message if the first value entered by the user is 0. */

function computeAverage(array){
    let sum = 0;

    for (let i=0; i < array.length; i++){
        sum += array[i];
    }
    let average = sum/(array.length);

    return average;
}   


const numbers = [];

while(true){
    let number = Number(prompt("Enter a number "));

    if (number === 0 && numbers.length === 0){
        alert("The first number can't be zero");
        continue;

    } else if (number === 0 && numbers.length != 0){
        alert("Bye!");
        break;
        
    } else {
        numbers.push(number);
        let average = computeAverage(numbers);

        alert(`The average is ${average}`);
    }

}
