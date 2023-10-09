using System;
using System.Collections.Generic;
using System.Linq;

// Variable Declarations
string message = "Hello, C#!";
int[] numberArray = { 1, 2, 3, 4, 5 };

// Functions
int AddNumbers(int a, int b)
{
    return a + b;
}

// Lambda Expressions
Func<int, int, int> MultiplyNumbers = (a, b) => a * b;

// Interfaces
interface IPerson
{
    string Name { get; set; }
    int Age { get; set; }
}

// Classes
class Animal
{
    public string Name { get; }

    public Animal(string name)
    {
        Name = name;
    }

    public void MakeSound(string sound)
    {
        Console.WriteLine($"{Name} says {sound}");
    }
}

// Inheritance
class Dog : Animal
{
    public string Breed { get; }

    public Dog(string name, string breed) : base(name)
    {
        Breed = breed;
    }

    public void WagTail()
    {
        Console.WriteLine($"{Name} is wagging its tail.");
    }
}

// Generics
T Identity<T>(T arg)
{
    return arg;
}

int num = Identity<int>(42);

// Enums
enum Color
{
    Red,
    Green,
    Blue
}

Color selectedColor = Color.Red;

// C# Features
(ValueType, int) tuple = ("C#", 3);
var dynamicType = 42;
object unknownType = "unknown";
string? nullableType = null;

// LINQ Query
var numbersGreaterThanTwo = from number in numberArray where number > 2 select number;

// Async/Await
async Task<string> FetchDataAsync()
{
    await Task.Delay(2000);
    return "Data has been fetched!";
}

async Task FetchAndLogDataAsync()
{
    var data = await FetchDataAsync();
    Console.WriteLine(data);
}

FetchAndLogDataAsync().Wait();
