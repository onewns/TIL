// developer.mozilla.org
'use strict';


// 2. Variable, rw (read, write)
// let (added in ES6)
let globalName = 'global name';
{
    let name = 'wonjun';
    console.log(name);
    name = 'hello';
    console.log(name);
}
console.log(name) // 접근 불가
console.log(globalName); // 전역 변수라 가능


// var hoisting (move declartion from bottom to top)
// has no block scope
{
    age = 4;
    var age;
}
console.log(age); // 가능...



// 3. constant r(read only)
// use const whenever possible
// only use let if variable needs to change.

// Note!
// Immutable data types: pribitive types, frozen objects (i.e. object.freeze())
// Mutabel data types: all objects by default are mutable in JS
// favor immutable data type always for a new reasons
// - security
// - thread safety
// - reduce human mistkaes
const daysInWeek = 7;
const maxNumber = 5;





// 4. Variable types
// pribitive, single item: number, string, boolean, null, undefiend, symbol
// object, box contariner
// function, first-class function


const count = 17; // integer
const size = 17.1; // decimal number
// 둘다 타입은 number => number로 모두 가능

// special numertic values
// position 등 쓰임새가 있음
const infiniy = 1 / 0;
const negativeInfinity = -1 / 0;
const nAn = 'not a number' / 2;


// bigInt(fairely ne, don't use in yet)
const bigInt = 123456789876543212345678765432n;
// type => bigint




// string
const char = 'c';
const brendad = 'brendan';
const helloB = `h1 ${brendad}`  // template literlas


// boolean
// false: 0, null, undefined, Nan, ''
// true: any other value


// null
let nothing = null;
// value = null, type = object


// undefined
let x;
// console.log(x) => undefined


// symbol, create unique idenrifiers for objects
const symbol1 = Symbol('id');
const symbol2 = Symbol('id');
// symbol1 === symbol2 => flase
const gSymbol = Symbol.for('id');
const gSymbo2 = Symbol.for('id');
// gSymbol1 === gSymbol2 => true
console.log(`value: ${symbol1.descriptioiny}`)

// object, real-life objdct, data structure
const w = {name:'wj', age:'29'}
w.age = 22;
// w.age 에 접근해서 변경은 가능



// 5. Dynamic typing: dynamically typed language
let text = 'hello';
// type = string
text = 1;
// type = number
text = '7' + 5;
// value = 75 type = string
text = '8' / '2';
// value = 4 type = number