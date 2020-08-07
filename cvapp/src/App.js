import React, { Component } from "react";
import { customConfig } from "./customConfig.js";
import FileUploadutil from "./components/FileUploadutil.js"
import CamCaptureutil from "./components/CamCaptureutil.js"

class App extends Component {
  render(){
    return(
      <div>
        <FileUploadutil customConfig={customConfig}/>
        <CamCaptureutil customConfig={customConfig}/>
      </div>
  )}
}

export default App;
