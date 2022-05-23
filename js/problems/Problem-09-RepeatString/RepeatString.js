/* Repeat String

Program a function that repeats a text X times, 
e.g. myFunction('Hello World', 3) will return Hello World Hello World Hello World Hello World*/

function repeatString(string, n) {
    return (string.trim() + ' ').repeat(n);
}

let string = prompt("insert string: ");

while(true){
    let n = Number(prompt("insert a number: "));

    if(!n){
        alert("Insert a number!");
        continue;

    } else if (n <= 0){
        alert("Number can't be negative or zero!");
        continue;

    } else{
        n = Math.round(n);
        alert(repeatString(string,n));
        break;
    }
}