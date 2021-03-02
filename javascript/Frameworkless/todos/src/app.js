import todos from './components/todos.js';
import todoFilter from './components/todoFilter.js';

import registry from './registry.js';

registry.add('todos', todos);
registry.add('todoFilter', todoFilter);

const state = {
  todos: [
    {
      title: 'react',
      completed: false,
    },
    {
      title: 'vue',
      completed: true,
    },
    {
      title: 'vanilla',
      completed: false,
    },
  ],
  currentFilter: 'all'
};

const events = {
  addItem: (title) => {
    state.todos.push(
      {
        title,
        completed: false
      }
    );
    render(state)
  },
  deleteItem: (index) => {
    state.todos.splice(index, 1);
    render(state);
  },
  toggleItemCompleted: (index) => {
    state.todos[index].completed = !state.todos[index].completed;
    render(state);
  },
  changeFilter: (filter) => {
    state.currentFilter = filter;
    render(state)
  }
};

const render = (state) => {
  window.requestAnimationFrame(() => {
    const element = document.querySelector('.main');
    const newElement = registry.renderRoot(element, state, events);
    element.replaceWith(newElement);
  })
};

export default () => {
  render(state)
};