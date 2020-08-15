import React, { Component } from "react";
import Webcam from "react-webcam";
import axios from "axios";

export default class CamCaptureutil extends Component {
  state = {
    imageCaptured: "",
    prediction: "",
    facingMode: "environment",
  };
  setRef = (webcam) => {
    this.webcam = webcam;
  };
  cameraHandler = () => {
    if (this.state.facingMode === "environment") {
      this.setState({
        facingMode: "user",
      });
    } else {
      this.setState({
        facingMode: "environment",
      });
    }
  };
  captureImageHandler = () => {
    const imageSrc = this.webcam.getScreenshot();
    this.setState({
      imageCaptured: imageSrc,
    });
    console.log(imageSrc);
  };
  uploadImageHandler = () => {
    if (this.state.imageCaptured === "") {
      this.setState({
        prediction: "No Image Camptured",
      });
    } else {
      var imageObj = {
        imageString: this.state.imageCaptured,
      };
      axios
        .post(
          this.props.customConfig.predictionUrl +
            "/getPredictionFromImageString",
          imageObj
        )
        .then((res) => {
          console.log(res.data);
          this.setState({
            prediction: res.data.result,
          });
        });
    }
  };
  render() {
    const videoConstraints = {
      width: 720,
      height: 720,
      facingMode: this.state.facingMode,
    };
    return (
      <div>
        <Webcam
          audio={false}
          height={64 * 6}
          ref={this.setRef}
          screenshotFormat="image/jpeg"
          width={64 * 6}
          mirrored={false}
          videoConstraints={videoConstraints}
        />
        <img src={this.state.imageCaptured} />
        <button onClick={this.cameraHandler}>Change Camera</button>
        <button onClick={this.captureImageHandler}> Capture </button>
        <button onClick={this.uploadImageHandler}> Predict </button>
        <span>
          <h3>{this.state.prediction}</h3>
        </span>
      </div>
    );
  }
}
