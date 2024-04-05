import React, {useEffect, useRef} from "react";
import {createPortal} from "react-dom";
import './modal.css'

export default function Phone(props) {
    const dialog = useRef()
    useEffect(() => {
        if (props.open) {
            dialog.current.showModal()
            console.log('Open Phone')
        }
        else {
            dialog.current.close()
            console.log('Close Phone')
        }

    }, [props.open]);
    return ( createPortal(
        <dialog ref={dialog}>
            {props.children}
            <div className='name'>
                <div className='img_avatar'>
                {props.photo ==null && <img className='avatar' src='https://autobuy.by/images/avatars/user.svg'/> || <img className='avatar' src={props.user.photo}/> }
                </div>
                <div>
                <p> {props.name} </p>
                <p className='price'> +375{props.phone}</p>
                </div>
            </div>
            <img src='https://autobuy.by/images/product/number.svg'/>
            <div className='warning'>
                <p> Никогда не отправляйте предоплату, риску финансового мошенничества подвержен каждый
                                четвертый владелец банковских карт.</p>
            </div>
        </dialog>, document.getElementById('modal')
        )
    )
}