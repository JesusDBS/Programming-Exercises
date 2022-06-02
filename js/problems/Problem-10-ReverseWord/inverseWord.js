//This function inverts the words of a text string, e.g. myFunction("Hola Mundo") will return "odnuM aloH".

const inverseWord = function (word){
    return word.trim().split(' ').reverse().join(' ')
}

export{ inverseWord }