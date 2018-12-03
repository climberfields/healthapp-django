import React, { Component } from 'react';
import './style.css';
import { Icon, Menu } from 'semantic-ui-react'
import Coffee from '../Coffee';

class Selection extends Component {
  render() {
    return (
      <div className="container">
        <div>
          <a href="/" className="logout">Logout</a>
        </div>

        <div className="innerSelection">

          <div id="coffeeDiv">
          <a href="/" className="logout">Logout</a>
            <button ><a href="/coffee">COFFEE</a></button>
          </div>

          <div id="alcoholDiv">
            <button ><a href="/alcohol">Alcohol</a></button>
          </div>


          <div id="summaryDiv">
            <button>Summary</button>
          </div>

        </div>
      </div>
    );
  }
}

export default Selection;


// <div id="coffeeDiv">
//   <input className="coffee" type="submit" value="Coffee"/>
// </div>
//
// <div id="alcoholDiv">
//   <input className="alcohol" type="submit" value="Alcohol"/>
// </div><br /><br />
//
// <div id="summaryDiv">
//   <input className="summary" type="submit" value="Summary"/>
// </div><br /><br />
