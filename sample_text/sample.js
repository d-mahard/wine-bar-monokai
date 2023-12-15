// Variables
var varVariable = "var";
let letVariable = "let";
const constVariable = "const";

// Function
function functionDeclaration(a, b) {
    return a + b;
}

// Arrow Function
const arrowFunction = (a, b) => a + b;

// Class
class MyClass {
    constructor(name) {
        this.name = name;
    }

    myMethod() {
        return this.name;
    }
}

// Object
const myObject = {
    key: "value",
    method: function() {
        return this.key;
    }
};

// Array
let myArray = [1, 2, 3, 4, 5];

// For loop
for (let i = 0; i < myArray.length; i++) {
    console.log(myArray[i]);
}

// While loop
let i = 0;
while (i < myArray.length) {
    console.log(myArray[i]);
    i++;
}

// Map, Filter, Reduce
myArray.map(x => x * 2);
myArray.filter(x => x > 2);
myArray.reduce((a, b) => a + b, 0);

// Promise
const myPromise = new Promise((resolve, reject) => {
    resolve("Success!");
});

// Async/Await
async function asyncFunction() {
    const result = await myPromise;
    console.log(result);
}

// Try/Catch
try {
    throw new Error("This is an error");
} catch (error) {
    console.log(error.message);
}