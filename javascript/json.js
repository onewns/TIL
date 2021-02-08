// JSON
// JavaScript Object Natation

// 1. Object to JSON
//stringfy(obj)
let json = JSON.stringify(true);
console.log(json);

json = JSON.stringify(['apple', 'banana']);
console.log(json);

const rabbit = {
  name: 'tori',
  color: 'white',
  size: null,
  birthDate: new Date(),
  jump: () => {
    console.log(`${this.name} can jump`);
  },
};

json = JSON.stringify(rabbit);
// 함수나 symbol 같은 경우는 json에 포함 x
console.log(json);

json = JSON.stringify(rabbit, ['name', 'color']);
console.log(json);

json = JSON.stringify(rabbit, (key, value) => {
  console.log(`key: ${key}, value: ${value}`);
  return key === 'name' ? 'nick' : value;
});
console.log(json);

// 2.JSON to Object
// parse(json)
json = JSON.stringify(rabbit);
const obj = JSON.parse(json, (key, value) => {
  console.log(`key: ${key}, value: ${value}`);
  return key === 'birthDate' ? new Date(value) : value; // 스트링화된 객체를 다시 생성
});
console.log(obj);
rabbit.jump();


// JSON Diff checker: http://www.jsondiff.com/​
// JSON Beautifier/editor: https://jsonbeautifier.org/​
// JSON Parser: https://jsonparser.org/​
// JSON Validator: https://tools.learningcontainer.com/json-validator/