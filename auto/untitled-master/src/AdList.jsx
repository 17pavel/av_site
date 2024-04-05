import './App.css';
import React from "react";

import Ad from "./Ad";

export default function CarList (props) {

const car = props.cars && props.cars

return (
        <div>

            {car.map(cars => <Ad cars={cars} key={cars.id}/>)}
        </div>
    )
}