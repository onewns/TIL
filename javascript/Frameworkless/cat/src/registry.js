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