import './App.css';
import Select from "./select";
import Mark from "./Mark";
import React, {useContext, useEffect, useState} from "react";
import axios from "axios";
import CarList from "./AdList";
import {SelectContex} from "./Main";
import Sity from "./modal/SIty";




let selcar;

const API_URL = 'http://127.0.0.1:8000/api/city/';
const API_CAR = 'http://127.0.0.1:8000/api/car/';

export default function AVContent(se) {
    const [citys, setCitys] = useState([]);
    const [cars, setCars] = useState([]);
    const [price,setPrice] = useState();
    const [priceat,setPriceat] = useState();
    const [modalsity,setModalsity] = useState(false);

        useEffect(() => {
    const fetchSity = async () => {
      try {
        const response = await axios.get(API_URL);
        setCitys(response.data);
      } catch (error) {
        console.error('Error fetching data:', error);
      }
    };

    fetchSity();
  }, []);

    useEffect(() => {

    const fetchData = async () => {
      try {
        const response = await axios.get(API_CAR);
        setCars(response.data);
      } catch (error) {
        console.error('Error fetching data:', error);
      }
    };

    fetchData();
  }, []);
    const {s1} = useContext(SelectContex);
    const {t1} = useContext(SelectContex);
    function Start() {
        s1(null)
        t1(null)

    }
    if (!se.se) {
        selcar=cars
    }

    if (se.ty==='Марка') {
            if (selcar) {selcar= selcar.filter((q) => q.mark_car === se.se)}
            else {selcar= cars.filter((q) => q.mark_car === se.se)}
        }


    if (se.ty==='Кузов') {
        selcar ? selcar = selcar.filter((q) => q.body === se.se) : selcar = cars.filter((q) => q.body === se.se)
    }
    if (se.ty==='Трансмиссия') {
        selcar = selcar.filter((q) => q.transmission === se.se)
    }

    if (se.ty ==='Двигатель') {
        selcar = selcar.filter((q) => q.motor ===se.se)
    }

    if (se.ty==='Привод') {
        selcar = selcar.filter((q) => q.drive === se.se)
    }
    if (se.ty==='Год от') {
        selcar = selcar.filter((q) => q.year >= se.se)
    }
    if (se.ty==='до ') {
        selcar = selcar.filter((q) => q.year <= se.se)
    }
    if (price) {
        selcar = cars.filter((q) => q.price>=price)
    }

    if (priceat) {
        selcar = cars.filter((q) => q.price<=priceat)
    }

    if (se.ty==='Объем от') {
        selcar = cars.filter((q) => q.volume >= se.se)
    }

    if (se.ty==='до') {
        selcar = cars.filter((q) => q.volume <= se.se)
    }


    const count = selcar.length

    function OpenSity() {
        setModalsity(true)
    }


    return(
        <div className='Av-content-body'>

            <div className='Av-content-head'>
                <h1>Объявления о продаже автомобилей в Беларуси</h1>
                <p>Автобай - бесплатно продать или купить авто с пробегом</p>
            </div>
            <div className='city'>
                Легковые автомобили

                <div className='city_region' >
                    <button className='butsity' onClick={OpenSity}>
                    <img src="https://autobuy.by/images/product/city.svg" width="10" height="10" margin='10'/>
                        <p>Вся Беларусь</p></button>

                        <Sity sity={citys} key={citys.id} open={modalsity}>
                            <button className='close' onClick={() => setModalsity(false)}>
                                X
                            </button>
                        </Sity>

                </div>
            </div>
            <div className='lin'>
                <div className='row'>
                    <div className='filter'>
                        {<Select cars={cars} key = {cars.id} hiden='Марка'/>}
                        {<Select cars={cars} key = {cars.id} hiden='Модель'/>}
                        {<Select cars={cars} key = {cars.id} hiden='Поколение'/>}

                        <input type='text' placeholder='Цена от' onChange={(e) => setPrice(e.target.value)}/>
                        <input type='text' placeholder='Цена до' onChange={(e) => setPriceat(e.target.value)}/>
                        <button>USD</button>
                        <button>BYN</button>
                        {<Select cars={cars} key = {cars.id} hiden='Объем от'/>}
                            {<Select cars={cars} key = {cars.id} hiden='до'/>}
                        {<Select cars={cars} key = {cars.id} hiden='Год от'/>}
                        {<Select cars={cars} key = {cars.id} hiden='до '/>}
                        {<Select cars={cars} key = {cars.id} hiden='Кузов'/>}
                        {<Select cars={cars} key = {cars.id} hiden='Привод'/>}
                        {<Select cars={cars} key = {cars.id} hiden='Двигатель'/>}
                        {<Select cars={cars} key = {cars.id} hiden='Трансмиссия'/>}
                        <p> <button onClick={Start}>Сбросить</button><span>Найдено {count} предложений</span></p>
                    </div>
                    <div>
                        <CarList cars = {selcar} key={selcar.id}/>
                    </div>
                </div>
                <div className='mark_sq'>
                <div>
            {Mark('https://autobuy.by/images/mark_logo/lada.svg', 'ВАЗ')}
                {Mark('https://autobuy.by/images/mark_logo/audi.svg', 'Audi' )}
                {Mark('https://autobuy.by/images/mark_logo/bmw.svg', 'BMW')}
                {Mark("https://autobuy.by/images/mark_logo/ford.svg", 'Ford')}
                </div>
                <div>
                {Mark("https://autobuy.by/images/mark_logo/hyundai.svg", 'Hyundai')}
                {Mark("https://autobuy.by/images/mark_logo/kia.svg", 'Kia')}
                {Mark("https://autobuy.by/images/mark_logo/mercedes-benz.svg", 'Mercedes-Benz')}
                {Mark("https://autobuy.by/images/mark_logo/mitsubishi-motors.svg", 'Mitsubishi')}
                </div>
            </div>
            </div>

        </div>
    )
}