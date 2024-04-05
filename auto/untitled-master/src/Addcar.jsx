import React, {useEffect, useState} from "react";
import axios from "axios";
import {Link} from "react-router-dom";
import './css/addcar.css'

const API_URL ='http://127.0.0.1:8000/api/car/';
const SITY_URL = 'http://127.0.0.1:8000/api/city/';

export default function Addcar() {
    const [mark,setMark] = useState();
    const [model,setModel] = useState();
    const [generation,setGeneration] = useState();
    const [drive,setDrive] = useState();
    const [transmition,setTransmition] = useState();
    const [motor,setMotor] = useState();
    const [price,setPrice] = useState();
    const [mileage,setMileage] = useState();
    const [volume,setVolume] = useState();
    const [year,setYear] = useState();
    const [vin,setVin] = useState(null);
    const [color, setColor] = useState();
    const [description,setDescription] = useState();
    const [photo,setPhoto] = useState();
    const [condition, setCondition] = useState();
    const [exchange, setExchange] = useState(false);
    const [sity,setSity] = useState();
    const [body,setBody] = useState();
    const [si,setSi] = useState('Минск');


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
    const sit = s && s.map((q) => q.name);
    const sity_cars = sity && sity.filter((n) => n.name === si)
    const sity_car = sity_cars && parseInt(sity_cars[0].id)
    console.log(sity_car)
    let ex = ''
    if (exchange) {
        ex = 'Возможен обмен'
    }
    else {ex = 'Без обмена'}
    const addNewCar = async () => {
  try {
      const newCar = {
          mark_car: mark,
          model_car: model,
          generation: generation,
          drive:drive,
          transmission: transmition,
          motor: motor,
          price: price,
          mileage: mileage,
          volume: volume,
          year: year,
          vin: vin,
          color: color,
          description: description,
          photo: photo,
          condition: condition,
          exchange: ex,
          city_car: sity_car,
          user: 72,
          body: body,
      };
    const response = await axios.post(API_URL, newCar);
    return (response.data)
  } catch (err) {
    console.error(err.toJSON())
  }


};

    const bod = ['Минивэн', 'Седан', 'Хэтчбек 3дв', 'Хэтчбек 5дв', 'Лифтбек', 'Внедорожник 3дв', 'Внедорожник 5дв',
    'Компактвэн', 'Универсал 5дв', 'Фургон'].sort()
    return (
        <div className='main'>
            <h1>Ведите данные машины</h1>
            <div className='param'>
                <div className='mark'>
                    <p><input placeholder='Марка' value={mark} onChange={(e) => setMark(e.target.value)}/></p>
                    <p><input placeholder='Модель' value={model} onChange={(e) => setModel(e.target.value)}/></p>
                    <p><input placeholder='Поколение' value={generation}
                              onChange={(e) => setGeneration(e.target.value)}/></p>
                </div>
                <div className='body'>
                    <p><select value={drive} onChange={(e) => setDrive(e.target.value)}>
                        <option hidden>Привод</option>
                        <option>Передний</option>
                        <option>Задний</option>
                        <option>Полный</option>
                    </select></p>
                    <p><select value={body} onChange={(e) => setBody(e.target.value)}>
                        <option hidden>Кузов</option>
                        {bod.map((q) => <option>{q}</option>)}
                    </select></p>
                    <p>
                        <select value={transmition} onChange={(e) => setTransmition(e.target.value)}>
                            <option hidden>Трансмиссия</option>
                            <option>Автомат</option>
                            <option>Вариатор</option>
                            <option>Механика</option>
                            <option>Робот</option>
                        </select>
                    </p>
                    <p>
                        <select value={motor} onChange={(e) => setMotor(e.target.value)}>
                            <option hidden>Мотор</option>
                            <option>Бензиновый</option>
                            <option>Дизельный</option>
                            <option>Электрический</option>
                            <option>Гибрид</option>
                        </select>
                    </p>
                </div>

                <div className='price'>
                    <p><input placeholder='Цена' value={price} onChange={(e) => setPrice(e.target.value)}/></p>
                    <p><input placeholder='Пробег' value={mileage} onChange={(e) => setMileage(e.target.value)}/></p>
                    <p><input placeholder='Объем двигателя' value={volume} onChange={(e) => setVolume(e.target.value)}/>
                    </p>
                    <p><input placeholder='Год выпуска' value={year} onChange={(e) => setYear(e.target.value)}/></p>
                    <p><input placeholder='VIN' value={vin} onChange={(e) => setVin(e.target.value)}/></p>
                    <p><input placeholder='Цвет' value={color} onChange={(e) => setColor(e.target.value)}/></p>
                    <p></p></div>
                <div className='sity'>
                    <select value={condition} onChange={(e) => setCondition(e.target.value)}>
                        <option hidden>Состояние</option>
                        <option>Новая</option>
                        <option>С пробегом</option>
                        <option>На разбор</option>
                    </select>
                    <p>
                        <select value={si} onChange={(e) => setSi(e.target.value)}>
                            <option hidden>Город</option>
                            {sit && sit.map((q) => <option>{q}</option>)}
                        </select>
                    </p>
                    <p>Обмен <input type='checkbox' placeholder='Обмен' checked={exchange}
                                    onChange={(e) => setExchange(!exchange)}/></p>
                </div>
            </div>
            <div className='param'>


            <p></p>
            <textarea className='des' placeholder='Описание' value={description}
                      onChange={(e) => setDescription(e.target.value)}></textarea>
            <p></p>
            <textarea className='des' placeholder='Фото' value={photo}
                      onChange={(e) => setPhoto(e.target.value)}></textarea>
            </div>
            <p></p>
            <Link to='/'>
                <button onClick={addNewCar}>Добавить объявление</button>
            </Link>

        </div>
    )
}
