
import './App.css';
import {Route, Routes} from "react-router-dom";
import React from "react";
import Main from "./Main";
import CarPage from "./CarPage";
import Autorisation from "./Autorisation";
import Addcar from "./Addcar";


function App() {

  return (

    <Routes >
        <Route path='/' element={<Main />}/>
        <Route path='car/:id' element={<CarPage/>}/>
        <Route path='autorisation/' element={<Autorisation/>}/>
        <Route path='addcar/' element={<Addcar/>}/>
    </Routes>
  );
}

export default App;
