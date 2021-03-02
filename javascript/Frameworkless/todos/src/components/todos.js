const getTodoElement = (todo, index, events, currentFilter) => {
  // 개별적으로 event를 추가하기 위해 HTML element 로 구성
  const todoElement = document.createElement('li');
  const checkBox = document.createElement('div');
  const textBox = document.createElement('span');
  const deleteBtn = document.createElement('button')

  const { title, completed } = todo;
  const { deleteItem, toggleItemCompleted } = events
  if (completed) {
    checkBox.classList.add('completed')
  }

  checkBox.innerText = `${completed}`
  textBox.innerText = `${title}`;
  deleteBtn.innerText = `삭제`;

  checkBox.addEventListener('click', () => { toggleItemCompleted(index) })
  deleteBtn.addEventListener('click', () => { deleteItem(index) })
  todoElement.appendChild(checkBox)
  todoElement.appendChild(textBox)
  todoElement.appendChild(deleteBtn)
  const frag = document.createDocumentFragment()
  if ((currentFilter === 'completed' && !completed) || (currentFilter === 'active' && completed)) {
    return frag
  } else {
    return todoElement
  }
}


export default (element, state, events) => {

  const { todos, currentFilter } = state;
  const { addItem } = events;
  const newTodosElement = element.cloneNode(true);
  newTodosElement.innerHTML = ''  // element 초기화
  const todoInput = document.createElement('input');
  newTodosElement.appendChild(todoInput);

  const todosElement = document.createElement('ul');
  todos.map((todo, index) => getTodoElement(todo, index, events, currentFilter)).forEach(
    element => { todosElement.appendChild(element) }
  )

  newTodosElement.appendChild(todosElement);

  todoInput.addEventListener('keypress', (e) => {
    if (e.key === 'Enter') {
      addItem(e.target.value);
    }
  })

  return newTodosElement
}