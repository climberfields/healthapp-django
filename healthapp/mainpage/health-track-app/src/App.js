import React, { Component } from 'react';
import logo from './logo.svg';
import './App.css';
import {Switch, Route} from 'react-router-dom';
// import HealthComponent from './HealthComponent';
import Login from './HealthComponent/Login'
import Coffee from './HealthComponent/Coffee'
import Alcohol from './HealthComponent/Alcohol'

import Selection from './HealthComponent/Selection'


class App extends Component {
  render() {
    return (
      <div className="App">
      <Switch>
          <Route exact path='/' component={Login} />
          <Route path='/selection' component={Selection} />
          <Route path='/coffee' component={Coffee} />
          <Route path='/alcohol' component={Alcohol} />
        </Switch>
      </div>
    );
  }
}

export default App;

// <Switch>
//   <Route exact path='/' component={Login} />
// </Switch>
