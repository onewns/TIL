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