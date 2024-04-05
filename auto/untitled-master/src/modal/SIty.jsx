import React, {useEffect, useRef} from "react";
import {createPortal} from "react-dom";
import './modal.css'


export default function Sity(props) {

    const dialog = useRef();
    const reg = props.sity && props.sity;
    const regset = new Set();
    reg.map(q => regset.add(q.region));
    const regarr = Array.from(regset).sort();


    function selectSity(n) {
    const q = reg.filter((w) => w.region===n)
        const a= q.map(w => w.name)
        return a.sort()
}

    useEffect(() => {
        if (props.open) {
            dialog.current.showModal()
        }
        else {
            dialog.current.close()
        }

    }, [props.open]);

    function Sityreg(r) {
        const s = selectSity(r);
        const sset = new Set();
        s.map(s => sset.add(s.name))
        const sarr = Array.from(sset).sort()
        return (
            <div>
                {sarr.map(sarr => <p>{sarr}</p>)}
            </div>
        )
    }

    const z = regarr.map(q =>  selectSity(q))
return (createPortal(
    <dialog ref={dialog}>
        {props.children}
        <div>
            <p>Выбирете город или область</p>
            <p>Вся республика</p>
            {regarr.map(sity => <p>{sity}{z.map(sity => <p>{sity}</p>)}</p>)}

        </div>
    </dialog>, document.getElementById('modal')
))
}