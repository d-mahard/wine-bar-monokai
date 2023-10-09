// Variable Declarations
let message: string = "Hello, TypeScript!";
const numberArray: number[] = [1, 2, 3, 4, 5];

// Functions
function addNumbers(a: number, b: number): number {
  return a + b;
}

// Arrow Function
const multiplyNumbers = (a: number, b: number): number => a * b;

// Interfaces
interface Person {
  name: string;
  age: number;
}

// Classes
class Animal {
  constructor(public name: string) {}

  makeSound(sound: string) {
    console.log(`${this.name} says ${sound}`);
  }
}

// Inheritance
class Dog extends Animal {
  constructor(name: string, public breed: string) {
    super(name);
  }

  wagTail() {
    console.log(`${this.name} is wagging its tail.`);
  }
}

// Generics
function identity<T>(arg: T): T {
  return arg;
}

const num: number = identity<number>(42);

// Enums
enum Color {
  Red,
  Green,
  Blue,
}

const selectedColor: Color = Color.Red;

// TypeScript Features
const tuple: [string, number] = ["TypeScript", 3];
const anyType: any = 42;
const unknownType: unknown = "unknown";
const nullableType: string | null = null;

// Promises
const fetchData = (): Promise<string> => {
  return new Promise((resolve) => {
    setTimeout(() => {
      resolve("Data has been fetched!");
    }, 2000);
  });
};

async function fetchAndLogData() {
  const data = await fetchData();
  console.log(data);
}

fetchAndLogData();
