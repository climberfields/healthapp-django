import React, { Component } from 'react';
import './style.css'
import Chart from './Chart';

class Alcohol extends Component {

  render() {
    return (
      <div className="Alcoholcontainer">
        <div className="chart"><Chart /></div>
      </div>
    );
  }
}

export default Alcohol;
