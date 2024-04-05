import React, {useContext} from 'react';
import {SelectContex} from "./Main";

export default function Mark(img,name) {
    const {s1} = useContext(SelectContex);
    const {t1} = useContext(SelectContex);
    function Mainicon () {
        s1(name);
        t1('Марка');

    }
    return (
    <div className='mark' onClick={Mainicon}>
        <img src={img}></img>
        <p>{name}</p>
    </div>)
}