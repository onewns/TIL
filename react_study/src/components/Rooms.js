import React from 'react'
import {Route, Link} from 'react-router-dom'

function Room({ match }) {
  console.log(match)
  return (
  <h2>{`${match.params.roomId}방을 선택하셨습니다.`}</h2>
  )
}

function Rooms({match}) {
  // console.log(match)
  return (
    <div>
      <h2>여기는 방을 소개하는 페이지 입니다.</h2>
      <Link to={`${match.url}/blueRoom/b`}>파란방 입니다.</Link><br/>
      <Link to={`${match.url}/greenRoom/a`}>초록방 입니다.</Link><br/>
      <Route path={`${match.url}/:roomId/:a`} component={Room}/>
      <Route
        exact
        path={match.url}
        render={() => <h3>방을 선택해 주세요.</h3>}
      />
    </div>
  );
};


export default Rooms;