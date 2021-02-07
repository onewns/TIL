// Objects
// one of the JavaScript's data types.
// a collection of related data and/or functionality.
// Nearly all objects in JavaScript are instance of Object
// object = { key : value };

// 1. Literals and properties
const obj1 = {}; // 'object literal' syntax
const obj2 = new Object(); // 'object constructor' syntax

function print(person) {
  console.log(person);
  console.log(person.name);
  console.log(person.age);
}

const nick = {name: 'nick', age: 4 };
print(nick);

// with JavaScript magic (dynamically typed language)
// can add properties later
nick.hasjob = true;
console.log(nick.hasjob);

// can delete properties later
delete nick.hasjob
console.log(nick.hasjob);


// 2. Computed properties
// key should be always string
console.log(nick['name']);
nick['hasjob'] = true;
console.log(nick.hasjob);

function printValue(obj, key) {
  console.log(obj.key); // undefined => obj에 key라는 key를 찾는것
  console.log(obj[key]);
}

printValue(nick, 'name');
printValue(nick, 'age');

// 3. Property value shorthand
const person1 = { name: 'bob', age: 2 };
const person2 = { name: 'steve', age: 3 };
const person3 = { name: 'dave', age: 4 };
const person4 = new Person('nick', 30);
console.log(person4);

// 4. Contructor Function
function Person(name, age) {
  // this = {};
  this.name = name;
  this.age = age;
  // return this
}


// 5. in operator: property existence check (key in obj)
console.log('name' in nick);
console.log('age' in nick);
console.log('random' in nick);


// 6. for..in vs for..of
// for (key in obj)
for (key in nick) {
  console.log(key);
}
// for (value of iterable)
const array = [1, 2, 4, 5];
for (value of array) {
  console.log(value)
}


// 7. Fun cloning
// Object.assign(dest, [obj1, obj2, obj3...])
const user = { name: 'nick', age: '20'}
const user2 = user;
user2.name = 'coder';
console.log(user); // user 까지 변경

// old way
const user3 = {};
for (key in user) {
  user3[key] = user[key];
}

const user4 = {};
Object.assign(user4, user);
console.log(user4);
const user5 = Object.assign({}, user);
console.log(user5);

// anoter example
const fruit1 = {color: 'red' };
const fruit2 = {color: 'blue', size: 'big' };
const mixed = Object.assign({}, fruit1, fruit2);  // 뒤에꺼로 덮어짐
console.log(mixed)