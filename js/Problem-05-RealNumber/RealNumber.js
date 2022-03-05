/*Real Number

Make a program that, given a real number given by the user, 
determines the number of integers digits and decimals that compose it. 
String methods are not allowed.*/

let number = Number(prompt("Insert a number: "));

if(number){
    let flag = true;
    let integerPart = [];
    let decimalPart = [];
    let decimalIdex = null;

    number = String(number);

    for(let character=0; character < number.length; character++){
        if(flag){
            if(number[character] === "."){
                flag = false;
                decimalIdex = character;
                break;
                
            } else{
                integerPart.push(number[character]);
            }
        }
    }

    decimalPart = number.slice(decimalIdex + 1, number.length);

    alert(`The integer part of ${number} is ${integerPart.length} long and its decimal part is ${decimalPart.length} long`)


} else if(number === 0){
    alert(`Number is ${number}`);
    
} else{
    alert("Please insert a number!");

}

