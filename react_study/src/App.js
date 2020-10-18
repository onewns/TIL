import React, {useEffect, useState} from 'react';
import './App.css';

import TodoList from './TodoList.js'



export default function App() {
  const [pageName, setPageName] = useState('');
  useEffect(() => {
    window.onpopstate = event => {
      setPageName(event.state);
    };
  }, []);
  const onClick1 = () => {
    const pageName = 'page1';
    window.history.pushState(pageName, '', '/page1');
    setPageName(pageName);
  }
  const onClick2 = () => {
    const pageName = 'page2';
    window.history.pushState(pageName, '', '/page2');
    setPageName(pageName);
  }
  return (
    <div className="App">
      <TodoList/>
      <div>
        <button onClick={onClick1}>page1</button>
        <button onClick={onClick2}>page2</button>
        {!pageName && <Home/>}
        {pageName === 'page1' && <Page1/>}
        {pageName === 'page2' && <Page2/>}
      </div>
    </div>
  );
}

function Home() {
  return <h2>여기는 홈페이지</h2>
}
function Page1() {
  return <h2>여기는 1</h2>
}
function Page2() {
  return <h2>여기는 2</h2>
}
