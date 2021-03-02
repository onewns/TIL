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
  filter: false
};

const events = {

};

const render = (element, state, events) => {
  window.requestAnimationFrame(() => {
    // const main = document.querySelector('.main');
    // const newMain = registry.renderRoot(main, state, events);
    const newElement = registry.renderRoot(element, state, events);
    element.replaceWith(newElement);
  })
};

export default (main) => {
  render(main, state, events)
};