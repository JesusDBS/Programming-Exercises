/*Number of character

Program a function that counts the number of characters in a text string, e.g. myFunction("Hello World") will return 10.*/

function CountCharacter(string) {
    alert(`The number of character is ${string.length}`)    
}

while(true){
    let string = prompt("Insert a string: ");

    if(Number(string)){
        alert("The string can't be a number");
        continue;
        
    } else{
        CountCharacter(string);
        break;
    }

    
}   


