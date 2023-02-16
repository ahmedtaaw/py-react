import logo from './logo.svg';
import './App.css';

import axios from 'axios';
import {useState, useEffect} from 'react';

function App() {

  const [people, setPeople] = useState([]);

  useEffect(()=>{
    axios.get('/api').then(res=>setPeople(res.data));
  },[])

  return people.map((p,index)=>{
     return <h3 key={index}>{p.id} {p.name} {p.age} </h3>
  })
}

export default App;
