# Redux



### 1. Action

> 앱에서 스토어로 보내는 데이터 묶음
> store.dispatch() 를 통해 보내기 가능
> 무슨일이 일어나는지에 대해 기술 => 일종의 메시지?

#### actions.js

```javascript
// 액션 타입
// 어떤 일을 할것인지 상수로 미리 설정?

export const ADD_TODO = 'ADD_TODO'
export const COMPLETE_TODO = 'COMPLETE_TODO'
export const SET_VISIBILITY_FILTER = 'SET_VISIBILITY_FILTER'

// 다른 상수

export const VisibilityFilters = {
  SHOW_ALL: 'SHOW_ALL',
  SHOW_COMPLETED: 'SHOW_COMPLETED',
  SHOW_ACTIVE: 'SHOW_ACTIVE'
}

// 액션 생산자
// 액션 타입(어떤 일을 수행하는지?) 과 parms를 리턴?

export function addTodo(text) {
  return { type: ADD_TODO, text }
}

export function completeTodo(index) {
  return { type: COMPLETE_TODO, index }
}

export function setVisibilityFilter(filter) {
  return { type: SET_VISIBILITY_FILTER, filter }
}
```



### 2. Reducer

> Action 이라는 메시지를 받으면
> 그 결과 상태가 어떻게 바뀌는지 특정하는 역할

- 인수가 주어지면, 다음상태를 계산 해서 반환x

#### reducer.js

```javascript
// 독립적인 리듀서를 만들고 한번에 묶어줄때 편한 도구
import { combineReducers } from 'redux';

// action 들을 불러옴
import { ADD_TODO, COMPLETE_TODO, SET_VISIBILITY_FILTER, VisibilityFilters } from './actions';


const { SHOW_ALL } = VisibilityFilters;

function visibilityFilter(state = SHOW_ALL, action) {
  switch (action.type) {
  case SET_VISIBILITY_FILTER:
    return action.filter;
  default:
    return state;
  }
}

function todos(state = [], action) {
  switch (action.type) {
  case ADD_TODO:
    return [...state, {
      text: action.text,
      completed: false
    }];
  case COMPLETE_TODO:
    return [
      ...state.slice(0, action.index),
      Object.assign({}, state[action.index], {
        completed: true
      }),
      ...state.slice(action.index + 1)
    ];
  default:
    return state;
  }
}

const todoApp = combineReducers({
  visibilityFilter,
  todos
});

export default todoApp;
```





### 3. Store

- 애플리케이션의 상태를 저장
- getState() 를 통해 상태에 접근
- dispatch(action) 를 통해 상태를 수정
- subscribe(listener) => 리스너를 등록?

※ 하나이 앱에서는 하나의 store 만

#### index.js

```javascript
import { createStore } from 'redux';
import todoApp from './reducers';

let store = createStore(todoApp);
```

