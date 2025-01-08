import logo from './logo.svg';
import './App.css';
import React from 'react';
// import Item from './MyItem';


class StarWars extends React.Component {
  constructor() {
    super()
    this.state = {
      name: null,
      height: null,
      image: "",
      weight: null,
    }
  }
  getNewCharacter() {
    const randNum = Math.ceil(Math.random()*87)
    const url = `https://akabab.github.io/starwars-api/api/id/${randNum}.json`
    fetch(url)
      .then(response => response.json())
      .then(data => { console.log(data)   
        this.setState({
      image: data.image,
      name: data.name,
      height: data.height,

      weight: data.mass,
      loadedCharacter: true,
      })


    })
  }
  render() {
    
    return (
    <div>
      {
        this.state.loadedCharacter &&
        <div> 
          <img src={this.state.image} alt="Not Available" width="200px" />
          <h1>{this.state.name}</h1>
      <p>{this.state.height} m</p>
      <p>weight: {this.state.weight} kg</p>
     
     
        </div>
      }
       <button 
      type="button" 
      onClick={() => this.getNewCharacter()}
      className="bn" 
      >
        Find Star Wars Character
      </button>
      </div>
    )
  }

}


function App() {
  return (
    <div className="App">
      <header className="App-header">

        <StarWars />





      </header>
    </div>
  );
}

export default App;
