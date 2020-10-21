import React,{useState, useEffect} from 'react'
import {BrowserRouter, Route, Link} from 'react-router-dom'
import MyRoute from './MyRoute'



const PropsExercise = ({match}) => {
  const [simpleProps,setSimpleProps] = useState(0)
  const [routeProps,setRouteProps] = useState(0)


  useEffect(() => {
    console.log("mount")
  },[])

  useEffect(() => {
    console.log("update")
  })

  console.log(match)
  return (
    <div>
      <Link to={`${match.url}/route`}>route</Link> <br/>
      <button onClick={() => setRouteProps(routeProps + 1)}>route+</button>
      <Route path={`${match.url}/route`}
        render={() => <MyRoute cnt={`${routeProps}`}/> }
      />
      <br/>
      <button onClick={() => setSimpleProps(simpleProps + 1)}>simple+</button>
      <MyRoute cnt={`${simpleProps}`}/>
    </div>
  )
}

export default PropsExercise