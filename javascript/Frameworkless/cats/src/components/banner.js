import catCard from './catCard.js';
import loading from './loading.js';

export default (element, { randomCats, bannerLoading }, events) => {
  const newElement = element.cloneNode(true);
  newElement.innerHTML = ``;
  if (randomCats) {
    randomCats = randomCats.slice(1, 2)
    randomCats.forEach((data) => {newElement.appendChild(catCard(data))})
  } else {
    newElement.innerHTML = loading();
  }
  return newElement
}