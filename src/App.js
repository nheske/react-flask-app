import React from 'react';
import ReactDOM from 'react-dom';
import Part from './Part.js';

const imagesPath = {
  minus: "black.png",
  plus: "green.png"
}


class App extends React.Component {
  constructor() {

   super();
//    const [imageHtml, setImageHtml] = useState(0);
  this.state = {
    open: true
  }

    fetch('/time').then(response => response.json()).then(data => console.log(data));
//    fetch('/green').then(response => response.text()).then(data => setImageHtml(data));
  }

    getImageName = () => this.state.open ? 'plus' : 'minus'

    toggleImage = () => {
    this.setState(state => ({ open: !state.open }))
  }

    changeColor = () => {
      this.setState({color: "black"});
    }

  render() {
    const imageName = this.getImageName();
    return (
      <div>
        <img style={{maxWidth: '50px'}} src={imagesPath[imageName]} onClick={this.toggleImage} />
            <Part />
      </div>
    );
  }

}

ReactDOM.render(<Part />, document.getElementById('root'));


export default App;