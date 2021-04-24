import React, {useState} from 'react';
import ReactDOM from 'react-dom';
import Part from './Part.js';
import { Typography } from "@material-ui/core";
import UploadFiles from "./components/upload-files.component";

class App extends React.Component{
  state = {url: ""}
  constructor() {
   super();
  }


    fetch_data = () => {
        fetch('api/time').then(res=>{
            if(res.ok){
                return res.json();
            }
            throw new Error('request failed');
        },networkError=> console.log(networkError.message)
        ).then(jsonRes=>{
            console.log(jsonRes)
//            this.setState({url: jsonRes[0].url});
            this.setState({url: jsonRes[0]})
        })
    }

  render() {
    return (
      <div>
        <img  src={this.state.url} alt='nothing'  />
        <button onClick={this.fetch_data}> Generate!</button>
            <Part />
        <div className="container">
              <UploadFiles />
        </div>
      </div>
    );
  }

}

ReactDOM.render(<Part />, document.getElementById('root'));

export default App;