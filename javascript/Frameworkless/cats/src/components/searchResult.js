import catCard from './catCard.js';
import loading from './loading.js';

export default (element, { cats, resultLoading }, events) => {
  const newElement = element.cloneNode(true);
  newElement.innerHTML = ``;
  if (!cats) {
    newElement.innerText = `검색해 주세요`;
  } else if (cats.length) {
    cats.forEach((cat) => {
      let cardElement = catCard(cat);
      cardElement.addEventListener('click', () => events.getCatDetail(cat.id))
      newElement.appendChild(cardElement)
    })
  } else if (cats.length === 0) { 
    newElement.innerText = `검색결과가 없어요`;
  }
  if (resultLoading) {
    newElement.innerHTML = loading()
  }
  return newElement
}