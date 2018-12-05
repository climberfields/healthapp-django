import React, { Component } from 'react';
import { Router, Route, Link, IndexRoute, hashHistory, browserHistory } from 'react-router'
import './style.css';

import Login from './Login';
import Coffee from './Coffee';
import Alcohol fro './Alcohol';
import Selection from './Selection';

class Main extends Component {
  render() {
    return (
      <div className="main">
        <h1>Main</h1>
        <Login />
        <Coffee />
        <Alcohol />
        <Selection />
      </div>
    );
  }
}

export default Main;
