
import React, {useEffect, useState} from "react";
import Tyt from "./AV";
import AVMenu from "./AV-menu";
import axios from "axios";

import CarPageMain from "./CarPageMain";




export default function CarPage() {

const ur = document.location.href.split('/')[4];
const API_URL = 'http://127.0.0.1:8000/api/car/'+ur.toString()+'/';

const SITY_URL = 'http://127.0.0.1:8000/api/city/';
    const [car, setCar] = useState([]);

    const [sity, setSity] = useState([]);




  useEffect(() => {
    const fetchData = async () => {
      try {
        const response = await axios.get(API_URL);
        setCar(response.data);
      } catch (error) {
        console.error('Error fetching data:', error);
      }
    };

    fetchData();
  }, []); // Пустой массив зависимостей означает, что useEffect будет выполнен только после монтирования компонента.



      useEffect(() => {
    const fetchDatasity = async () => {
      try {

        const response = await axios.get(SITY_URL);
        setSity(response.data);
      } catch (error) {
        console.error('Error fetching data:', error);
      }
    };

    fetchDatasity();
  }, []);
    return (
        <div>
            <Tyt/>
            <AVMenu/>

            <div className='Av-content-body'>
                <div className='filter2' >


                    {<CarPageMain  car={car} key={car.id} sity={sity} key={sity.id} />}

                </div>
            </div>
        </div>
    )
}