//Check Palindrome
//Program a function that validates if a given word or phrase is a palindrome 
//(read the same in one direction as in the other), e.g. mifuncion("Salas") will return true

import { inverseWord as inverse} from "../Problem-10-ReverseWord/inverseWord.js";

while(true){
    let word = prompt('insert a string: ');

   if(!(/[a-zA-Z]/).test(word)){
       alert("This is not a word!")
       continue;

   }else{
       if(word.toLocaleLowerCase().replace(/\s/g,'') === inverse(word).replace(/\s/g,'').toLocaleLowerCase()){
        alert(`Your string "${word}" is a palindrome!`);
        break;
       }
   }
}