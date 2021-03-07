'use strict';
// class 속성(filed), 행동(methods)


// class
// - template
// - declare once
// - no data in

// object
// - instance of a class
// - created many times
// - data in

// Object-oriented programming
// calss: template
// object: instance of a class
// JavaScript classes
// - introduced in ES6
// - syntactical sugar over prototype-based inheritance


// 1. Class declarations
class Person {
  // constructor
  constructor (name, age) {
      this.name = name;
      this.age = age;
  }
  // methods
  speack() {
    console.log(`${this.name}: hello!`);
  }
}

const nick = new Person('nick', 20);
console.log(nick.name);
console.log(nick.age);
nick.speack();


// 2. Getter and setters
class User {
  constructor(firstName, lastName, age) {
    this.firstName = firstName;
    this.lastName = lastName;
    this.age = age;
  }
  // this.age => get age() 를 호출
  // = age; => set age(value) 를 호출
  // _age를 쓰지 않으면 무한정 스택이 쌓임

  get age() {
    return this._age;
  }

  set age(value) {
    // if (value < 0) {
      // throw Error('age can not be negative');
    // }
    this._age = value < 0 ? 0 : value;
  }
}

const user1 = new User('nick', 'cage', -1);
console.log(user1.age);


// 3. Fields (public, private)
// Too soon!
class Experiment {
  // 외부에서 접근 가능
  publicField = 2;

  // 외부에서 접근 불가
  #priviateField = 0;
}

const experiment = new Experiment();
console.log(experiment.publicField);
console.log(experiment.privateField);


// 4. Static properties and methods
// Too soon!
class Article {
  static publisher = 'Dream Coding';
  constructor(articleNumber) {
    this.articleNumber = articleNumber;
  }

  static printPublisher() {
    console.log(this)
    console.log(this.publisher);
    console.log(Article.publisher);
  }
}

const article1 = new Article(1);
const article2 = new Article(2);
console.log(article1.publisher);
console.log(Article.publisher);
Article.printPublisher();


// 5. Inheritance
// a way for one class to extend another class.
class Shape {
  constructor(width, height, color) {
    this.width = width;
    this.height = height;
    this.color = color;
  }

  draw() {
    console.log(`drawing ${this.color} color!`);
  }

  getArea() {
    return this.width * this.height
  }
}

class Rectangle extends Shape {}
class Triangle extends Shape {
  draw() {
    super.draw();
    console.log('triangle');
  }
  getArea() {
    return (this.width * this.height) / 2;
  }
}

const rectangle = new Rectangle(20, 20, 'blue');
rectangle.draw();
console.log(rectangle.getArea());
const triangle = new Triangle(20, 20, 'red');
triangle.draw();
console.log(triangle.getArea());


// 6. Class checking: intanceIf
console.log(rectangle instanceof Rectangle); // true
console.log(triangle instanceof Rectangle); // false
console.log(triangle instanceof Triangle); // true
console.log(triangle instanceof Shape); // true
console.log(triangle instanceof Object); // true