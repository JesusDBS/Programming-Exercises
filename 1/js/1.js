/* Hello:

Write a program that asks the user to enter his or her name. The program should
respond with a message that says hello to the user, using his or her name. */

const prompt = require("prompt-sync")({ sigint: true});

const userName = prompt("What's your name? ");
console.log(`Hello ${userName}!`);