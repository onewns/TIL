const appendFilterButtons = (element, events) => {
  const { changeFilter } = events;
  const allButton = document.createElement('button');
  const activeButton = document.createElement('button');
  const completedButton = document.createElement('button');

  allButton.addEventListener('click', () => { changeFilter('all') })
  activeButton.addEventListener('click', () => { changeFilter('active') })
  completedButton.addEventListener('click', () => { changeFilter('completed') })

  allButton.innerText = 'all'
  activeButton.innerText = 'active'
  completedButton.innerText = 'completed'

  element.appendChild(allButton)
  element.appendChild(activeButton)
  element.appendChild(completedButton)
  return element
}

export default (todoFilterElement, state, events) => {
  const newTodoFilterElement = todoFilterElement.cloneNode(true);
  newTodoFilterElement.innerHTML = ``
  
  return appendFilterButtons(newTodoFilterElement, events)
}