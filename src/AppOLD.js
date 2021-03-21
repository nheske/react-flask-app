import React from 'react';
import ReactDOM from 'react-dom';
import Part from './Part.js';

const imagesPath = {
  minus: "black.png",
  plus: "green.png"
}


class App extends React.Component {
  last_response = "black.png"

  constructor() {
   super();
//    const [imageHtml, setImageHtml] = useState(0);
  this.state = {
    open: true,
    last_response : "black.png"
  }

 //   fetch('/img').then(response => response.json()).then(data => console.log(data));
//    fetch('/green').then(response => response.text()).then(data => setImageHtml(data));
  }

//    getImageName = () => this.state.open ? 'plus' : 'minus'
    getImageName = () => this.state.last_response


  toggleImage = () => {
    console.log("fetching..")
    fetch('/img')
        .then(response => {
            response.text();
            console.log("received response.."+response.text())
            this.setState(state => ({ last_response: response.text() }))
        })
//        .then(data => console.log(data));
//    this.setState(state => ({ open: !state.open }))
  }
//    toggleImage = () => {
//    fetch('/img')
//        .then(response => response.text())
//        .then(data => console.log(data));
//    this.setState(state => ({ open: !state.open }))
//  }
//  promise1.then((value) => {
//  console.log(value);
//  // expected output: "Success!"
//});

  changeColor = () => {
    this.setState({color: "black"});
  }

  render() {
    console.log("render invoked..")
    const imageName = this.getImageName();
    alert(imageName)
    return (
      <div>
        <img style={{maxWidth: '50px'}} src={imagesPath[imageName]} alt='nothing'  />
        <button onClick={this.toggleImage}>Get Image</button>
            <Part />
      </div>
    );
  }

}

ReactDOM.render(<Part />, document.getElementById('root'));


export default App;