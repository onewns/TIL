// Q1. make a string out of an array
{
  const fruits = ['apple', 'banana','orange'];
  
  // let answer = '';
  // for (fruit of fruits) {
  //   answer += fruit;
  // }
  // console.log(answer);
  
  
  // join
  const result = fruits.join(' and ');
  console.log(result);
}

// Q2. make an array out of a string
{
  const fruits = 'apple, banana, orange';
  const result = fruits.split(', ', 2);
  console.log(result);
}


// Q3. make this array look like this: [5, 4, 3, 2, 1]
{
  const array = [1, 2, 3, 4, 5];
  array.reverse();
  console.log(array);
}


// Q4. make new array without the first two elements
{
  const array = [1, 2, 3, 4, 5];
  const result = array.slice(2);
  console.log(result);
  // splice는 원본 배열 자체를 변경
}

class Student {
  constructor(name, age, enrolled, score) {
    this.name = name;
    this.age = age;
    this.enrolled = enrolled;
    this.score = score;
  }
}
const students = [
  new Student('A', 29, true, 45),
  new Student('B', 28, false, 80),
  new Student('C', 30, true, 90),
  new Student('D', 40, false, 66),
  new Student('E', 18, true, 88),
];

// Q5. find a student with the score 90
{
  const result = students.filter(student => student.score === 90);
  console.log(result);
  const answer = students.find(student => student.score === 90);
  console.log(answer);
}

// Q6. make an array of enrolled students
{
  const result = students.filter(student => student.enrolled);
  console.log(result);
}

// Q7. make an array contaning only the students' scores
// result should be: [45, 80, 66, 88]
{
  const result = students.map(student => student.score);
  console.log(result);
}

// Q8. check if there is a student with the score lower than 50
{
  const result = students.find(student => student.score <= 50);
  console.log(result);
  const answer = students.some(student => student.score <= 50);
  console.log(answer);
  // every는 모든 요소들이 만족해야 할 때
}

// Q9. compute students' average score
{
  const result = students.reduce((prev, curr) => prev + curr.score, 0) / students.length;
  console.log(result);
}

// Q10. make a string sorted in ascending order
// result should be: '45, 66, 80, 88, 90'
{
  const scores = students
    .map(student => student.score)
    .sort((a, b) => a -b)
    .join();
  console.log(scores);
}