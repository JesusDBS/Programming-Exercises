/*Cut text

Program a function that returns the trimmed text according to the number of characters indicated, 
e.g. myFunction("Hello World", 4) will return "Hello".*/

function cutText(string, n) {
    return string.slice(0,n)
}

let string = prompt("insert a string: ");

while(true){
    let n = Number(prompt("insert a number: "));
    if(n > string.length){
        alert("n can't be larger than string");
        continue;

    }else if(n < 0){
        alert("n can't be negative");
        continue;
    }
    alert(cutText(string,n));
    break;
}