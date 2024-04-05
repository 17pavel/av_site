import './App.css';
import {Link} from "react-router-dom";
import {useEffect, useState} from "react";
import axios from "axios";




const SITY_URL = 'http://127.0.0.1:8000/api/city/';

export default function Ad(props) {

    const [sity, setSity] = useState([]);
const sq = 'car/'
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


    const s = sity && sity;
    const si = s && s[props.cars.city_id-4];
    const sit = si && si.name;

    return (
        <div className='ad'>
            <div className='img_ad'>
            <img src={props.cars.photo.split('~')[0]} className='img_car'/>
            </div>
            <div className='data_car'>

                <Link to={sq + props.cars.id}><h3>
                    <strong>{props.cars.mark_car} {props.cars.model_car} {props.cars.generation}</strong></h3></Link>

                <span>
                {props.cars.volume} / {props.cars.motor} / {props.cars.year} г.
            </span>
                <span></span>
                <span>
                    {props.cars.mileage} км / {props.cars.transmission} / {props.cars.body}
                </span>
                <div>
                    <span className='vin'>{props.cars.vin && 'VIN ' + props.cars.vin.slice(0,6)+'**********'}</span>
                </div>
                <div className='city_ad'>
                    <img width="10" height="10" src="https://autobuy.by/template/autobuy/assets/icon/cursor.svg" ></img> {sit}
                </div>
            </div>

            <span className='price_byn'>{props.cars.price} р </span>
        </div>
    )
}