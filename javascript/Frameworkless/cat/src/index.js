import app from 'app.js'; // app === 렌더링 함수를 export

const baseComponent = (tagName, componentName) => {
  const component = document.createElement(tagName);
  component.dataset.component = componentName;  // 후에 registry 사용을 위해
  main.appendChild(component);
};

const main = document.querySelector('.main');
baseComponent('div', 'componentName');

app()