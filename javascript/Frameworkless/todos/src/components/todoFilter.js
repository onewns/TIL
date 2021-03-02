export default (todoFilterElement, state, events) => {
  const newTodoFilterElement = todoFilterElement.cloneNode(true);
  newTodoFilterElement.innerHTML = `
    <button>all</button>
    <button>active</button>
    <button>completed</button>
  `
  return newTodoFilterElement
}