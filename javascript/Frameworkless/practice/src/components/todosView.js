export default ($target, {todos}, events) => {
  const todosView = document.createElement('ul');
  todosView.dataset.component = 'todos';

  let todoElements = ''
  const getTodo = (todo) => {todoElements += `
  <li ${todo.completed ? 'class="completed"' : ''}>
    <div class="view">
      <input
        ${todo.completed ? 'checked' : ''}
        class="toggle"
        type="checkbox">
        <label>${todo.title}</label>
        <button class="destroy">삭제</button>
    </div>
    <input class="edit" value="${todo.title}">
  </li>
  `}
  todos.forEach(getTodo)
  todosView.innerHTML = todoElements
  return todosView
}