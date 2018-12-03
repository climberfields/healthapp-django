import React, { Component } from 'react';
import './style.css'
import Chart from './Chart';

class Coffe extends Component {

  render() {
    return (
        <div>
          <div className="dropdown">
            <span>Fun Facts</span>
            <div className="dropdown-con">
              <p>fghjkghhhh</p>
            </div>
          </div>
          <section><Chart/></section>
        </div>
    );
  }
}

export default Coffe;
