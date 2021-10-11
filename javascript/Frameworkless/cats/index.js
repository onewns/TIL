import app from './src/app.js';

const baseComponent = (tagName, componentName) => {
  const component = document.createElement(tagName);
  component.dataset.component = componentName
  main.appendChild(component)
};

const main = document.querySelector('.main');

baseComponent('h1', 'header')
baseComponent('section', 'searchBar');
baseComponent('section', 'banner');
baseComponent('section', 'searchResult');
baseComponent('div', 'catDetail');

app()