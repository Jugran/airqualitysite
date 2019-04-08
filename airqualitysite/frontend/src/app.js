import React, { Component } from "react";
import axios from "axios";

export default class app extends Component {
  constructor(props) {
    super(props);
    this.state = {
      data: []
    };
  }

  componentDidMount(props) {
    axios
      .get("/api/Country")
      .then(res => res.data)
      .then(data => {
        console.log("data:-", data);
        const some = data.map(key => {
          console.log("name:-", key.name);
          return (
            <div key={key.code}>
              <p>{key.name}</p>
            </div>
          );
        });
        this.setState({
          data: some
        });
      });
  }

  render() {
    return (
      <div>
        <div className="jumbotron bg-light">IN THE REACT..</div>
        {this.state.data}
      </div>
    );
  }
}
