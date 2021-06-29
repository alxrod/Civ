import React, { Component } from "react";
import axios from "axios";

class App extends Component {
  constructor(props) {
    super(props);
    this.state = {
      articleList: [],
      curArtIndex: 0,
    };
  }

  componentDidMount() {
    this.refreshList();
  }

  refreshList = () => {
    axios
      .get("/api/articles/")
      .then((res) => this.setState({ articleList: res.data}))
      .catch((err) => console.log(err));
  };

  renderItems = () => {

    return this.state.articleList.map((item, index) => (
      <li
        key={item.id}
        className="list-group-item d-flex justify-content-between align-items-center"
      >
        <span
          className={"article-title mr-2"}
          title={item.summary}
          onClick={() => this.setState({curArtIndex: index})}
        >
          {item.title}
        </span>
      </li>
    ));
  };

  renderSelected = () => {
    if (this.state.articleList.length > 0) {
      return (
        <div>
          <h5>{this.state.articleList[this.state.curArtIndex].title}</h5>
          <a href={this.state.articleList[this.state.curArtIndex].url}>Read More</a>
          <p>{this.state.articleList[this.state.curArtIndex].summary}</p>
        </div>
      )
    } else {
      return (<p></p>)
    }
  }

  render() {
    return (
      <main className="container">
        <h1 className="text-center my-6">Civ Articles</h1>
        <div className="row">
          <div className="col w-50 p-3">
            <div className="card p-3">
              <ul className="list-group list-group-flush border-top-0" style={{overflow:"scroll", height: "65vh"}}>
                {this.renderItems()}
              </ul>
            </div>
          </div>
          <div className="col w-50 p-3">
            <div className="card p-3 h-100">
              {this.renderSelected()}
            </div>
          </div>
        </div>
      </main>
    );
  }
}

export default App;