export default (element, { cat, catDetailVisible }, events) => {
  const newElement = element.cloneNode(true);
  newElement.innerHTML = ``;
  newElement.className = `${catDetailVisible ? 'visible' : 'none'}`;
  newElement.innerText = `${cat ? cat : '로딩중'}`;
  const closeButton = document.createElement('button');
  closeButton.innerText = '닫기';
  closeButton.addEventListener('click', () => {events.closeCatDetail()})
  newElement.appendChild(closeButton);

  const onClose = (keyEvent) => {
    console.log(keyEvent.key, catDetailVisible)
    if (keyEvent.key === 'Escape') {
      events.closeCatDetail()
    }
  }

  if (catDetailVisible) {
    window.addEventListener('keyup', events.closeCatDetailEsc)
  } else {
    window.removeEventListener('keyup', events.closeCatDetailEsc)
  }
  return newElement
}