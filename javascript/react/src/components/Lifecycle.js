import React,{useState, useEffect} from 'react'
import styled from 'styled-components'

const Box = styled.div`
  height:300px;
  width:300px;
  background-color:black;
`

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