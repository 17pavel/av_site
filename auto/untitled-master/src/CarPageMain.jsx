import React, {useEffect, useState} from "react";
import Phone from "./modal/Phone";
import axios from "axios";


const SITY_URL = 'http://127.0.0.1:8000/api/city/';
const USER_URL = 'http://127.0.0.1:8000/api/user/';

export default function CarPageMain(props) {
    const [sity, setSity] = useState([]);
    const [user,setUser] = useState([]);
    const [modal, setModal] = useState(false);
    const usercar = props.car.user && props.car.user;


    const photoUrl_ALL = props.car && props.car.photo || '' ;

    const photoUrl_Arr = photoUrl_ALL.split('~');


    // console.log(usercar)

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

    useEffect(() => {
    const fetchDataus = async () => {
      try {
        const response = await axios.get(USER_URL);
        setUser(response.data);
      } catch (error) {
        console.error('Error fetching data:', error);
      }
    };

    fetchDataus();
  }, []); // Пустой массив зависимостей означает, что useEffect будет выполнен только после монтирования компонента.

    const s = sity && sity;
    const si = s && s[props.car.city_id-4];
    const sit = si && si.name;

    const owner = user && user.filter(us => us.id===usercar);
    const id = owner.map(i => i.id);
    const name = owner.map(i => i.name);
    const phone = owner.map(i => i.phone)
    const photo = owner.map(i =>i.photo);

    // console.log(user[owner])


    function OpenPhone(){
    setModal(true)
}

    return (<div className='main'>
            <div className='imgs_car'>
                <p><strong>{props.car.mark_car} {props.car.model_car} {props.car.generation}</strong></p>
                <div className='main_img'>
                <img className='img_main' src={photoUrl_Arr[0]}/>
                </div>
                <div>
                    {photoUrl_Arr.map(arr => (
                        <img className='img_min' src={arr}/>
                    ))}
                </div>
                <div className='description'>
                    <p><strong>Описание</strong></p>
                    <p>{props.car.description}</p>
                </div>
                <div>
                    <p><strong>VIN код</strong></p>
                    <p>{props.car.vin && props.car.vin || 'VIN не указан'}</p>
                </div>
            </div>
            <div className='param'>
                <p className='price_byn'><strong>{props.car.price} р </strong></p>
                <div className='car_param'>
                    <div className='car_param_name'>
                        <p>Объем двигателя </p>
                        <p>Тип двигателя </p>
                        <p>Привод </p>
                        <p>Коробка передач </p>
                        <p>Кузов </p>
                        <p>Пробег </p>
                        <p>Год выпуска </p>
                        <p>Состояние </p>
                        <p>Цвет авто </p>
                    </div>
                    <div className='car_param_value'>
                        <p>{props.car.volume}</p>
                        <p>{props.car.motor}</p>
                        <p> {props.car.drive}</p>
                        <p>{props.car.transmission}</p>
                        <p>{props.car.body}</p>
                        <p>{props.car.mileage} км</p>
                        <p>{props.car.year} год</p>
                        <p>{props.car.condition}</p>
                        <p>{props.car.color}</p>
                    </div>
                </div>
                <div className='user'>
                    <p>{name[0]} </p>
                    <p>г. {sit}</p>
                        <button onClick={OpenPhone} className='button_phone'>Показать контакты</button>
                    <Phone name={name[0]} phone={phone[0]} photo={photo[0]} key={id[0]} open={modal}>
                        <button className='close' onClick={() => setModal(false)}>X</button>
                    </Phone>
                </div>
            </div>
        </div>
    )
}


