// Reverse word:
// Program a function that inverts the words of a text string, e.g. myFunction("Hello World") will return "odnuM aloH".

const inverseWord = function (word){
    return word.trim().split(' ').reverse().join(' ')
}

while(true){
    let word = prompt('insert a word: ');

   if(!(/[a-zA-Z]/).test(word)){
       alert("This is not a word!")
       continue;

   }else{
       alert(inverseWord(word));
       break;
   }
}