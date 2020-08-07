import React, { Component } from 'react';
import axios from "axios";


export default class FileUploadutil extends Component {
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
    if(this.state.fileSelected === null){
      this.setState({
        prediction : "No File Selected"
      });
    }
    else{
      const fd = new FormData();
      fd.append("image", this.state.fileSelected, this.state.fileSelected.name);
      axios.post(this.props.customConfig.predictionUrl+"/getPredictionFromImageFile", fd).then((res) => {
        console.log(res.data);
        this.setState({
          prediction : res.data.result
        });
      });
    }

  };

  render() {
    return (
      <div className="App">
        <input type="file" onChange={this.fileSelectHandler} />
        <button onClick={this.fileUploadHandler}> Predict </button>
        <span>
          <h3>{this.state.prediction}</h3>
        </span>
      </div>
    );
  }
}
