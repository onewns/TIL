const getTodoElements = (todos) => {
  let htmlSting = '';
  todos.forEach((todo) => {
    htmlSting += `
      <li class="todo-item">
        <button>${todo.completed}</button>
        <h4>${todo.title}</h4>
      </li>
    `
  })
  return htmlSting
}


export default (element, state, events) => {

  const { todos } = state

  const newTodosElement = element.cloneNode(true);
  const todoInput = document.createElement('input');
  newTodosElement.appendChild(todoInput);

  const todosElement = document.createElement('ul');
  todosElement.innerHTML = getTodoElements(todos);
  newTodosElement.appendChild(todosElement);

  return newTodosElement
}