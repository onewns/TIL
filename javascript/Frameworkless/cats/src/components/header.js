export default (element, state, events) => {
  const newElement = element.cloneNode(true);
  newElement.innerHTML = ``;
  newElement.innerText = '고양이 찾기!'
  return newElement
}