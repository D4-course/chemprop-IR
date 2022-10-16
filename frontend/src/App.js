import logo from './logo.svg';
import './App.css';
import MyForm from './form';
import Plot from 'react-plotly.js';
import react from 'react';
import axios from 'axios';


function App() {
  const [dataplot,setdata] = react.useState([
    {
      x: [1, 2, 3,4,4],
      y: [2.019033, 6, 3,4.5,4],
      type: 'scatter',
      mode: 'lines+markers',
      marker: {color: 'red'},
    },


  ]);
 
  const [name, setName] = react.useState("");
  const [isPred, setPred] = react.useState(false);

  
  const handleSubmit = (event) => {
    event.preventDefault();
    // var data = JSON.stringify(name);
    console.log(name);
    axios.post('http://127.0.0.1:8000/pred', {
      "smiles" : name,
    },
    {mode: 'no-cors'})
    .then(function (response) {
      let avg_preds = response.data['avg_preds'];
      setPred(true)
      setdata([
      {
        x: Array.from({length: 1801}, (_, i) => 2*i + 400),
        y: avg_preds,
        type: 'scatter',
        mode: 'lines',
        marker: {color: 'blue'},
      },
      


    ]);
    })
    .catch(function (error) {
      console.log("error ");
    });
    // alert(`The name you entered was: ${name}`)
  }
  console.log(isPred);
  return (
    // console.log("abfe");
    
    <div className="App">
      <header className="App-header">

      <form onSubmit={handleSubmit}>
        <label>Enter Smiles String
          
        </label><br></br>
        <input 
            type="text" 
            value={name}
            onChange={(e) => {setName(e.target.value)}}
          /><br></br>
        <input type="submit" value='predict' />
      </form>
      <p></p>
      <div>
      {isPred ? 
      (
      <Plot
      data={dataplot}
        layout={ {width: 800, height: 600, title: 'IR prediction'} }
        />):
        (<></>)
        }
      </div>
      </header>

    </div>
  );
}


export default App;
