export default (element, state, events) => {
  const newElement = element.cloneNode(true);
  newElement.innerHTML = ``;
  const searchInput = document.createElement('input');
  searchInput.autofocus = true;
  searchInput.addEventListener('keypress', (e) => {
    if (e.key === 'Enter') {
      events.getCats(e.target.value)
      e.target.value = '';
    }
  })
  const history = document.createElement('ul')
  state.keywords.forEach((keyword) => {
    const k = document.createElement('li');
    k.innerText = keyword
    k.addEventListener('click', () => events.getCats(keyword))
    history.appendChild(k);
  });

  newElement.appendChild(searchInput);
  newElement.appendChild(history);
  return newElement
}