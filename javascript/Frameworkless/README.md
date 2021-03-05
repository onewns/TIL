# Frameworkless Front-end



### 1. rendering

1. index.js
사용할 컴포넌트들을 생성후 **`main`** HTML Element에 부착
   
   ```js
   import app from 'app.js'; // app === 렌더링 함수를 export
   
   const baseComponent = (tagName, componentName) => {
     const component = document.createElement(tagName);
     component.dataset.component = componentName;  // 후에 registry 사용을 위해
     main.appendChild(component);
   };
   
   const main = document.querySelector('.main');
   baseComponent('div', 'componentName');
   
   app()
   ```
   
2. app.js

   ```js
   // component === (element, state, events)를 인자로 받아 element를 리턴하는 함수
   import component from 'component.js';
   
   // component의 호출 및 렌더링을 간편하게 하기 위한 설정 (add, renderRoot 함수를 반환)
   import registry from 'registry.js';
   
   // api 요청을 필요로 하는 함수
   import api from 'api.js'
   
   registry.add('componentName', component);  // 레지스트리에 함수를 저장
   
   
   // 렌더링 함수
   // element, state, event를 받아 새로운 element를 반환 후 원래 element와 교체
   const render = (state) => {
       const main = document.querySelector('.main')
       const newMain = registry.renderRoot(main, state, events);
       main.replaceWith(newMain);
   };
   
   
   // 상태 및 이벤트
   const state = {
   };
   
   const events = {
   };
   
   
   // index.js 에서 app()으로 호출되는 함수
   export default () => {
     render(state)
   };
   ```
   
3. registry.js

   ```js
   // 컴포넌트를 반환하는 함수들을 담아두는 객체
   // key로 data-component를 사용
   const registry = {};
   
   
   // root 밑에 있는 컴포넌트들을 순차적으로 교체
   const renderWrapper = component => {
     return (targetElement, state, events) => {
       const element = component(targetElement, state, events);
       const childComponents = element
       .querySelectorAll('[data-component]');
       Array.from(childComponents).forEach(target => {
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
   
   // registry에 등록을 위한 함수
   const add = (name, component) => {
     registry[name] = renderWrapper(component);
   };
   
   
   // root를 렌더링
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
       
     const childElement = document.createElement('div');
     newElement.appendChild(childElement);
   
     const stringHTML = document.createElement('ul');
     stringHTML.innerHTML = `
   	<li>1</li>
   	<li>2</li>
   	<li>3</li>
   	<li>4</li>
     `;
     newElement.appendChild(stringHTML);
       
     // 새로운 노드를 반환
     return newElement
   }
   ```
   
5. api.js

   ```js
   // url 관리
   const BASE_URL = 'https://'
   
   // 응답을 적절히 처리
   const parseResponse = async response => {
     const { status } = response;
     let data = null
     if (status === 200) {
       data = await response.json()
     } else if (status === 500) {
       alert('서버에 문제가 발생했습니다 다시 시도해주세요')
     } else if (status === 404) {
       alert('잘못된 요청입니다.')
     }
     return {
       status,
       data
     }
   }
   
   // 요청
   const request = async url => {
     const response = await fetch(url)
     return parseResponse(response)
   }
   
   // api 요청 모음
   const api = {
     async functionName() {
       const response = await request(`${BASE_URL}/url`)
       return response.data
     }
   }
   
   export default api
   ```

   