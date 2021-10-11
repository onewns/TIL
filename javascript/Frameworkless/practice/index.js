import headerView from './src/components/headerView.js';
import todoInputView from './src/components/todoInputView.js';
import todosView from './src/components/todosView.js';
import todoFilterView from './src/components/todoFilterView.js';

import registry from './registry.js';

import modelFactory from './src/model/model.js'

const model = modelFactory

registry.add('header', headerView)
registry.add('todoInput', todoInputView)
registry.add('todos', todosView)
registry.add('todoFilter', todoFilterView)


const state = {
  todos: [
    {
      title:'adfdsf',
      completed: false
    }
  ],
  option: 'all'
}

const events = {
  deleteItem: (index) => {
    state.todos.splice(index, 1);
    render();
  },
  addItem: (title) => {
    state.todos.push({
      title,
      completed: false
    })
    render(state);
  }
}

const makeComponent = (tagName, componentName) => {
  const component = document.createElement(tagName);
  component.dataset.component = componentName;
  components.push(component)
};
const components = [];
makeComponent('div', 'header')
makeComponent('input', 'todoInput')
makeComponent('ul', 'todos')
makeComponent('div', 'todoFilter')
const main = document.querySelector('.main')
components.forEach(component => main.appendChild(component))

const render = (state) => {
  window.requestAnimationFrame(() => {
    const main = document.querySelector('.main')
    const newMain = registry.renderRoot(main, state, events)
    main.replaceWith(newMain)
  })
}

render(state)