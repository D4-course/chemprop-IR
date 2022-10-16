import axios from 'axios';
import {React,useState} from 'react';

function MyForm() {
    const [name, setName] = useState("");
  
    const handleSubmit = (event) => {
      event.preventDefault();
      var data = JSON.stringify(name);
    //   console.log(data);
    var data = "abc";
      axios.post('http://localhost:3001/', {
        dataval : name,
      })
      .then(function (response) {
        console.log(response);
      })
      .catch(function (error) {
        console.log("error ");
      });
      alert(`The name you entered was: ${name}`)
    }
  
    return (
      <form onSubmit={handleSubmit}>
        <label>Enter your name:
          <input 
            type="text" 
            value={name}
            onChange={(e) => setName(e.target.value)}
          />
        </label>
        <input type="submit" />
      </form>
    )
  }

  export default MyForm;
  