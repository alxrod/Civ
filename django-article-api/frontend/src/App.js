import React, { Component } from "react";
import axios from "axios";

class App extends Component {
  constructor(props) {
    super(props);
    this.state = {
      articleList: [],
      curArtIndex: 0,
      queryState: "TOP",
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

  getCategoryColor = (id) => {
    let colors = ["#e6e6ea","#fe4a49","#2ab7ca","#FF9900","#7952B3","#2541B2","#FF7600","#FF005C","#064420","#D62AD0","#480032"]
    console.log(id)
    return colors[id]
  }

  compareArticles(art1, art2) {
    if (art1.hn_rank == -1) {
      return 1
    }

    if (art2.hn_rank == -1) {
      return -1
    }
    if (art1.hn_rank < art2.hn_rank) {
      return -1
    }
    if (art1.hn_rank > art2.hn_rank) {
      return 1
    }
    return 0
  }

  getArticles = () => {

  }

  renderItems = () => {

    return this.state.articleList.sort((art1, art2) => {
        return this.compareArticles(art1, art2)
    }).map((item, index) => (
      <div
        key={item.id}
        className="card d-flex justify-content-between p-2 mb-2"
        style={{"borderColor": this.getCategoryColor(item.category)}}
      >
        <span
          className={"article-title mr-2"}
          style={{"color": this.getCategoryColor(item.category)}}
          title={item.summary}
          onClick={() => this.setState({curArtIndex: index})}
        >
          {item.title}
        </span>
      </div>
    ));
  };



  renderSelected = () => {
    if (this.state.articleList.length > 0) {
      return (
        <div style={{height: "65vh"}}>
            <h5>{this.state.articleList[this.state.curArtIndex].title}</h5>
            <div style={{"height": "85%","overflow-y": "scroll", "overflow-x": "hidden"}}>
              <a className="pr-1" href={this.state.articleList[this.state.curArtIndex].url}>Read More</a>
              <a className="text-danger">Flag Summary</a>
              <p>{this.state.articleList[this.state.curArtIndex].summary}</p>
            </div>
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
            <div className="card">
              <ul className="nav">
                <li className="nav-item">
                  <a className="nav-link active" href="#">Top</a>
                </li>
                <li className="nav-item">
                  <a className="nav-link" href="#">Recent</a>
                </li>
                <li className="nav-item">
                  <a className="nav-link" href="#">Custom</a>
                </li>
              </ul>
              <div className="pb-3 pl-3 pr-3 pt-0">
                <ul className="list-group list-group-flush border-top-0" style={{"overflow-y": "scroll", "overflow-x": "hidden", "height": "65vh"}}>
                  {this.renderItems()}
                </ul>
              </div>
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