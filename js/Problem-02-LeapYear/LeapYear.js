/*Leap Year:

Given a year by the user, determine if it is leap, regular, or secula.*/

let year = Number(prompt("Enter a Year: "));

console.assert(year > 0, "A year can't be zero or negative!");

if (year <= 0){
    alert(`year must be greater than zero`);
} else {
    if (year%400 === 0){
        alert(`${year} is a Secular Year and Leap Year too!`);
    
    } else if (year%100 === 0){
        alert(`${year} is Secular Year!`);
    
    } else if (year%4 === 0){
        alert(`${year} is a Leap Year!`);

    } else {
        alert(`${year} is a Regular Year`);
    }
}

