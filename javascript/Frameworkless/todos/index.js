import app from './src/app.js';

const header = `<h1>TODO!</h1>`

const makeComponent = (tagName, componentName) => {
  const component = document.createElement(tagName);
  component.dataset.component = componentName;
  main.appendChild(component);
};

const main = document.querySelector('.main');
main.innerHTML = header;
makeComponent('div', 'todos');
makeComponent('div', 'todoFilter');

app(main)