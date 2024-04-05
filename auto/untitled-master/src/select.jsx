import React, {useContext, useState} from 'react';
import {SelectContex} from "./Main";


export default function Select (props) {
    const [carmark, setCarmark] =useState(false)
    const [carm, setCarm] = useState()
    const mark = props.cars && props.cars || 'Не найдено';
    const marks = new Set();

    mark.map(mark => marks.add(mark.mark_car));
    const m = Array.from(marks).sort();


    const trans = new Set()
    mark.map(mark => mark.transmission && trans.add(mark.transmission))
    const t = Array.from(trans).sort()

    const ye = new Set();
    mark.map(mark => mark.year && ye.add(mark.year));
    const y = Array.from(ye).sort();
    const ny = Array.from(ye).sort().reverse();
    const vol = new Set();
    mark.map(mark => mark.volume && vol.add(mark.volume));
    const v = Array.from(vol).sort();
    const nv = Array.from(vol).sort().reverse();
    const bod = new Set();
    mark.map(mark => mark.body && bod.add(mark.body));
    const b = Array.from(bod).sort();
    const dr = new Set();
    mark.map(mark => mark.drive && dr.add(mark.drive));
    const d = Array.from(dr).sort();
    const mot = new Set();
    mark.map(mark => mark.motor && mot.add(mark.motor));
    const mo = Array.from(mot).sort();
    const modl = []

    const {s1} = useContext(SelectContex);
    const {t1} = useContext(SelectContex);


    return (
            <select onChange={(e) => {
                s1(e.target.value);
                t1(props.hiden);


                }
            }>
                <option hidden> {props.hiden} </option>
                {props.hiden === 'Марка' && m.map( m => <option onChange={(e) =>{setCarm(true); setCarm(e.target.value)}}> {m} </option>)  }
                {props.hiden === 'Модель' && mark.map(mark => <option>{mark.model_car}</option>) }
                {props.hiden ==='Поколение' && mark.map(mark => <option>{mark.generation}</option>) }
                {props.hiden ==='Объем от' && v.map(v => <option>{v}</option>) }
                {props.hiden ==='до' && nv.map(nv => <option>{nv}</option>) }
                {props.hiden ==='Год от' && y.map(y => <option>{y}</option>) }
                {props.hiden ==='до ' && ny.map(ny => <option>{ny}</option>) }
                {props.hiden ==='Кузов' && b.map(b => <option>{b}</option>) }
                {props.hiden ==='Привод' && d.map(d => <option>{d}</option>) }
                {props.hiden ==='Двигатель' && mo.map(mo=> <option>{mo}</option>) }
                {props.hiden ==='Трансмиссия' && t.map(t => <option>{t}</option>) }
            </select>

    )
}