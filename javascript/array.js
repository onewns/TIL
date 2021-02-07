'use strict';

// Array

// 1. Declaration
const arr1 = new Array();
const arr2 = [1, 2];

// 2. Index position
const fruits = ['a', 'b'];


// 3. Loopint over an array
// print all fruits
// a. for
for (let i = 0; i < fruits.length; i++) {
  console.log(fruits[i]);
}
// b. for of
for (let fruit of fruits) {
  console.log(fruit);
}
// c. forEach
fruits.forEach( fruit =>console.log(fruit))


// 4. Addtion, deletion, copy
// push: add an item to the end
fruits.push('c', 'd', 'e', 'f', 'g');
console.log(fruits)

// pop: remove an item from the end
fruits.pop()
console.log(fruits)

// unshift: add an item to th beginning
fruits.unshift('0');
console.log(fruits);

// shift: remove an item from the benigging
fruits.shift();
fruits.shift();
console.log(fruits)

// note!! shift, unshift are slower than push, pop
// splice: remove an item by index position
fruits.splice(1, 1);
console.log(fruits)
fruits.splice(1, 1, 'j', 'j');
console.log(fruits)

// combine two arrays
const fruits2 = ['q', 't', 'm'];
const newFruits = fruits.concat(fruits2);
console.log(newFruits);


// 5. Searching
// find the index
console.log(fruits);
console.log(fruits.indexOf('f'));
console.log(fruits.indexOf('q')); // 없으면 -1

// includes
console.log(fruits.includes('z'));

// lastIndexOf
// indexOf 는 앞에서 찾고 끝 lastIndexOf는 마지막꺼 리턴