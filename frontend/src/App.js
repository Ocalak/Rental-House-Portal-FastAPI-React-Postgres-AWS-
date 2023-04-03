
import './App.css';
import React, {useState} from "react";

import Login from "./form/Login";
import Register from './form/Register';
import House from "./form/CreateHouse";
import HouseTable from './form/Housetable';
import GoogleMap from './form/GoogleMap';
import Home from './form/Home';
import { Link } from 'react-router-dom';

 

function App() {
  const[page, setPage]= useState("login");

  const chosePage = () => {
    if (page ==="login"){
      return <Login setPage={setPage} />;
    }
    if (page ==="register"){
      return <Register setPage={setPage} />;
    }
    if (page ==="createhouse"){
      return <House setPage={setPage} />;
    }
    if (page ==="houses"){
      return <HouseTable setPage={setPage} />;
    };
    /*
    if (page ==="home"){
      return <Home setPage={setPage} />;
    }; */
    /*
    if (page ==="googlemap"){
      return <GoogleMap setPage={setPage} />;
    };
    */

  };


  /*return chosePage();*/
  return chosePage()
            
  /*return  (   <div>
         <h1>House Listings</h1>
         <HouseTable />
       </div>
     );*/
   
   
};

export default App;


