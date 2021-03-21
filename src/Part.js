//import React, {useState, useEffect } from 'react';
import React from 'react';
import ReactDOM from 'react-dom';

class Car extends React.Component {
  render() {
    return " subpart";
  }
}

class Part extends React.Component {
  render() {
    return (
      <div>
        part:
      <Car />
      </div>
    );
  }
}

ReactDOM.render(<Part />, document.getElementById('root'));


export default Part;
