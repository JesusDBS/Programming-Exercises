/*Ork Planet:

Ork, Mork's home planet, celebrates the great planetary celebration every 8 years, similarly every 72 years 
Orson's birthday is celebrated, and to make it big it is celebrated the following year as well, 
but every 48 years the celebration that could have taken place that year is suspended due to the painful memory left by 
the defeat with his enemy planet in the Unholy Wars. Make a program to find out if a given year is a holiday or not.*/

let year = Number(prompt("Insert a Year: "));

if (year <= 0){
    alert("Year can't be negative or zero!");

} else{
    if(year%48 == 0){
        alert(`${year} is not year of celebration`);

    } else if(year%8 == 0 || (year -1)%72 ==0){
        alert(`${year} is a year of celebration!`);

    } else{
        alert(`${year} is not year of celebration`);
    }

}

