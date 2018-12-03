import React, { Component } from 'react';
import './style.css'
class Login extends Component {
  render() {
    return (
      <div className="container">

        <div className="login">
          <form>
            <input className="info" type="text" placeholder="username" /><br/>
            <input className="info" type="password" placeholder="password" /><br/>
            <button className="infoBtn"><a href="/selection">Login</a></button><br/>
          </form>
        </div>

        <div className="register">
          <form>
            <input className="info" type="text" placeholder="username" /><br/>
            <input className="info" type="password" placeholder="password" /><br/>
            <button className="infoBtn">Register</button><br/>
          </form>
        </div>
      </div>
    );
  }
}

export default Login;
