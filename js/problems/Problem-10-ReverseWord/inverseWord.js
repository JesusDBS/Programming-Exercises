//This function inverts the words of a text string, e.g. myFunction("Hola Mundo") will return "odnuM aloH".

const inverseWord = function (word){
    let words = word.trim().split('').reverse().join('');
    return words
}

export{ inverseWord }