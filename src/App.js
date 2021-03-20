import React from 'react';
import ReactDOM from 'react-dom';
import Garage from './Garage.js';

class App extends React.Component {
  constructor() {
    super();
    this.state = {color: "red"};
    fetch('/time').then(response => response.json()).then(data => console.log(data));
    fetch('/image').then(response => response.text()).then(data => console.log(data));
  }

  render() {
    return (
      <div>
      <h1>What about that Garage?</h1>
      <Garage />
      </div>
    );
  }
}

ReactDOM.render(<Garage />, document.getElementById('root'));


export default App;