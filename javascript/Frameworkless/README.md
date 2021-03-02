# Frameworkless Front-end



### 1. rendering

1. index.js 에서 사용할 컴포넌트들을 생성후 **`main`** HTML Element에 부착

   ```js
   import app from './src/app.js';
   
   const header = `<h1>TODO!</h1>`
   
   const makeComponent = (tagName, componentName) => {
     const component = document.createElement(tagName);
     component.dataset.component = componentName;  // 후에 registry 사용을 위해
     main.appendChild(component);
   };
   
   const main = document.querySelector('.main');
   main.innerHTML = header;
   makeComponent('div', 'todos');
   makeComponent('div', 'todoFilter');
   
   app(main)
   ```

2. app.js

   ```js
   // todos, todoFilter === 컴포넌트를 반환하는 함수
   import todos from './components/todos.js';
   import todoFilter from './components/todoFilter.js';
   
   // todos, todoFilter의 호출을 간편하게 하기 위한 설정
   import registry from './registry.js';
   
   registry.add('todos', todos);
   registry.add('todoFilter', todoFilter);
   
   
   // 상태 및 이벤트
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
   
   
   // 렌더링 함수
   // element, state, event를 받아 새로운 element를 반환 후 원래 element와 교체
   const render = (element, state, events) => {
     window.requestAnimationFrame(() => {
       // registry를 통해 새로운 element를 생성
       const newElement = registry.renderRoot(element, state, events);
       element.replaceWith(newElement);
     })
   };
   
   
   // index.js 에서 app()으로 호출되는 함수
   export default (main) => {
     render(main, state, events)
   };
   ```

3. registry.js

   ```js
   // 컴포넌트를 반환하는 함수들을 담아두는 객체
   // key로 data-component를 사용
   const registry = {};
   
   
   // registry에 등록을 위한 함수
   const add = (name, component) => {
     registry[name] = renderWrapper(component);
   };
   
   
   // root 밑에 있는 컴포넌트들을 순차적으로 교체
   const renderWrapper = component => {
     return (targetElement, state, events) => {
       const element = component(targetElement, state, events);
       const childComponents = element
       .querySelectorAll('[data-component]');
       Array
       .from(childComponents)
       .forEach(target => {
         const name = target.dataset.component;
         const child = registry[name];
         if (!child) { 
           return 
         }
   
         target.replaceWith(child(target, state, events))
       });
       return element;
     }
   };
   
   // root를 기준으로 컴포넌트를 교체
   const renderRoot = (root, state, events) => {
     const cloneComponent = root => {
       return root.cloneNode(true);
     };
     return renderWrapper(cloneComponent)(root, state, events);
   };
   
   export default {
     add,
     renderRoot
   }
   ```

4. component.js

   ```js
   export default (element, state, events) => {
     // 노드를 복사후
     const newElement = element.cloneNode(true);
     // 노드를 모두 비우기
     newTodoElement.innerHTML = '';
     // 비우지 않으면 appendChild 에서 문제가 생김
      
     const Input = document.createElement('input');
     newElement.appendChild(Input);
   
     const list = document.createElement('ul');
     list.innerHTML = `
   	<li>1</li>
   	<li>2</li>
   	<li>3</li>
   	<li>4</li>
     `;
     newElement.appendChild(list);
       
     // 새로운 노드를 반환
     return newElement
   }
   ```
   
   