import React from 'react';
import './App.css';
import {BrowserRouter, Route, Link} from 'react-router-dom'

import TodoList from './components/TodoList'
import Rooms from './components/Rooms'
import Profile from './components/Profile'
import Lifecycle from './components/Lifecycle'

export default function App() {
  return (
    <BrowserRouter>
      <div style={{padding:20, botder:`5px solid grey`}}>
        <Link to="/">홈</Link> <br/>
        <Link to="/photo">사진</Link> <br/>
        <Link to="/rooms">방 소개</Link> <br/>
        <Link to="/profile">프로필</Link> <br/>
        <Link to="/todolist">할일</Link> <br/>
        <Link to="/lifecycle">LifeCycle</Link><br/>
        {/* exact 의 의미
        exact 를 쓰지 않으면 /로 시작하는 경우 항상 렌더링 */}
        <Route exact path="/" component={Home}/>
        <Route path="/photo" component={Photo}/>
        <Route path="/rooms" component={Rooms}/>
        <Route path="/profile" component={Profile}/>
        <Route path="/todolist" component={TodoList}/>
        <Route path="/lifecycle" component={Lifecycle}/>
      </div>
    </BrowserRouter>
  );
}

function Home({ match }) {
  return <h2>여기는 홈페이지</h2>
}
function Photo({ match}) {
  return <h2>여기는 사진</h2>
}
