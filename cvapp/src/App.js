import React, { Component } from "react";
import axios from "axios";
import { customConfig }from "./customConfig.js";
import Webcam from "react-webcam";
class App extends Component {
  state = {
    fileSelected: null,
    prediction: ''
  };
  fileSelectHandler = (props) => {
    console.log(props.target.files[0]);
    this.setState({
      fileSelected: props.target.files[0],
    });
  };

  fileUploadHandler = () => {
    const fd = new FormData();
    fd.append("image", this.state.fileSelected, this.state.fileSelected.name);
    axios.post(customConfig.predictionUrl, fd).then((res) => {
      console.log(res.data);
      this.setState({
        prediction : res.data.result
      });
    });
  };

  render() {
    return (
      <div className="App">
        <input type="file" onChange={this.fileSelectHandler} />
        <button onClick={this.fileUploadHandler}> UPLOAD </button>
        <span>
          <h3>{this.state.prediction}</h3>
        </span>
      </div>
    );
  }
}

export default App;
