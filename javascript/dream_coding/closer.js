var fruits = ['apple', 'banana', 'peach'];
var $ul = document.createElement('ul');
var alertFruitBuilder = function (fruit) {
  return function (mouseEvent) {
      console.log(mouseEvent)
      alert(`your choice is ${fruit}`);
  };
};
fruits.forEach(function (fruit) {
var $li = document.createElement('li');
$li.innerText = fruit;
$li.addEventListener('click', alertFruitBuilder(fruit));
$ul.appendChild($li);
});
document.body.appendChild($ul)