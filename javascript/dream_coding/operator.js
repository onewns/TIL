// 1. string concatenation
console.log('my' + ' cat'); // my cat
console.log('1' + 2); // 12
console.log(`string literals: 1 + 2 ${1 + 2}`);

// 2. Numeric operator


// 3. Increment and decrement operators
let counter = 2;
const preIncrement = ++counter;  // 3
// counter = counter + 1
// preIncrement = counter 
const postIncrement = counter++; // 3
// postIncrement = counter
// counter = counter + 1


// 4. Assignment operators
let x = 3;
let y = 6;
x += y; // etc  


// 5. Comparison operators
// <, etc


// 6. Logical operators: ||, &&, !
const value1 = true;
const value2 = 4 < 2;

// || (or), finds the first truthy value
// value1 에서 끝남 => 복잡한 애를 뒤에 배치
console.log(`or: ${value1 || value2 || check()}`);

function check() {
    for (let i = 0; i < 10; i++) {
        console.log('adsjflsakdj')
    } return true
}
// && (and), finds the first false value



// 7. Equality
const stringFive = '5';
const numberFive = 5;

// == loose equality, with type conversion
// ===  strict equlaity, no type conversion

// object equality by reference
const ellie1 = {name: 'ellie'}
const ellie2 = {name: 'ellie'}
const ellie3 = ellie1
console.log(ellie1 == ellie2); // false
console.log(ellie1 === ellie2);  // false
console.log(ellie1 === ellie3); // true
// null == undefined   true


// 8. Conditional operators: if
// if, else if, else
const who = 'who';
if (who == 'who' ) {
    
} else {
    
}


// 9. Ternary operator: ?
// condition ? value1 : value2; 


// 10. Switch statement
// use for multiple if checks
// use for enum-like value check
// use for multiple type checks in TS
const browser = 'IE';
switch (key) {
    case value:
    case value1:
        break;

    default:
        break;
}


// 11. Loops
// while => 우리가 아는 while
// do while => 한번은 실행
// for => 우리가 아는 for
// continue, break => 아는것과 같음