// Count Word:
// Program a function to count the number of times a word is repeated in a long text,
// e.g. myFunction("hello world good-bye world", "world") will return 2

const countWord = function(string, word){
    let r = new RegExp(word,'ig');
    let n = string.match(r);

    if(!n) return false;
    
    return n.length
    
}

while(true){
    let string = prompt('Insert your string: ');
    let word = prompt('Insert the word you want to count: ');

    let n = countWord(string, word);

    if(n){
        alert(`There is ${n} ${word} in the string`);
        break;

    } else alert("The word you entered doesn't exits in the string!");

}