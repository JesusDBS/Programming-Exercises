/* String to Array

Program a function that given a String will return an Array of texts separated by a certain character, 
e.g. myFunction('hello world', ' ') will return ['hello', 'world'].*/

function splitString(string, character) {
    return string.split(character)
}

let string = prompt("insert a string: ");

while(true){
    let character = prompt("insert a character: ");

    if(!(string.includes(character))){
        alert("character must be part of the string!");
        continue;

    }
    alert(splitString(string, character));
    break;
}