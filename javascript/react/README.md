# React



## export VS export default

### 1. export

- 파일 전체가 아닌 특정 함수를 export 할때(모듈에서 주로 사용할듯)
- 함수의 이름이 명시적인 경우
- 다른 이름을 쓰려면 as를 써야함
- 한번에 여러개의 함수를 export 가능

```react
// export 방법 1
// 함수를 모두 정의해 놓고 한번에 export
function 함수1(parms) {}
function 함수2(parms) {}
function 함수3(parms) {}

export {함수1, 함수2, 함수3}



// export 방법 2
//함수를 한개 씩 export
export function 함수1(parms) {}
export function 함수2(parms) {}
export function 함수3(parms) {}



//import 방법
import {함수1, 함수3} from 'react'
```



### 2. export default

- 파일 전체를 export 할 때(컴포넌트 수준에서 많이 사용할듯)
- as 를 쓸 필요가 없음
- 기본적으로 익명함수로 사용

```react
// export 방법 1
// export default 자체를 익명함수로 만들기
export default (parms) => {}


//방법 2 => 익명함수를 변수에 저장한후 변수를 export
const 함수1 = (parms) => {}
export default 함수1


// import 방법
import 내가사용할이름 from 경로
```



## Props

1. simple 한 경우

   ```react
   // 해당 컴포넌트에 변수명과 함께 직접 전달
   
   const Component = (props) => {}
   <Component 속성명=전달할값/>
   ```

   

2. route를 통한 전달

   ```react
   import {Route} from 'react-router-dom'
   
   const Component = (props) => {}
   // render 함수를 사용!
   <Route path=경로 render={() => <Component 속성명=전달할값/>}/>
   ```

   

## Lifecycle

useEffect를 사용해서 구현

```react
// useEffect 의 기본구성
useEffect((parms) => {
    실행할함수,
    지겨보고 있을 값 // 배열의 형태로 추가
})


// 예시
const NumOfUpdate = () => {
  const [count1,setCount1] = useState(0);
  const [count2,setCount2] = useState(0);
    
  useEffect(() => {
    console.log('mount') // 밑에 지켜보고 있는 값이 없기 때문에 처음에만 실행
  },[]); // mount 시 지켜보고 있을 값이 필요 없음
    
  useEffect(() => {
    console.log('update') // update 마다 실행되는 함수
  },[count1,count2]); // 지켜보고 있다가 다시 렌더링하는 상황 확인
    
  return (
    <div>
      <p>count : {count1}</p>
      <p>count1: {count2}</p>
      <button onClick={() => setCount1(count1 + 1)}>count1 +</button>
      <button onClick={() => setCount2(count2 + 1)}>count2 +</button>
    </div>
  )
}

export default NumOfUpdate
```

