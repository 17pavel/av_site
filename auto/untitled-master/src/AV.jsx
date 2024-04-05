import './App.css';
import {Link} from "react-router-dom";

function Tyt() {
    return (<div>
            <header className="Av-header">
                <a href=''>
                <img className='Av-logo' src='https://autobuy.by/favicon.svg'/></a>
                <img className='Av-name' src='https://autobuy.by/autobuy_logo.svg'/>
                    <div className='ring'>
                        <div className='one'>

                    <img className='Av-bell' src='https://autobuy.by/images/notice/color/header_not.svg' />
                            <div className='one_bell'>
                        <span>1</span>
                            </div>
                        </div>
                    <p>Уведомления</p>
                    </div>
                <div>
                    <Link to='autorisation/'>
                    <button className='Av-but-reg' >Войти</button></Link>
                    <Link to='addcar/'>
                    <button className='Av-but-buy'>Продать</button></Link>

                </div>


            </header>
            <div>
                <hr className='line'/>
            </div>
        </div>

    );
}


export default Tyt;

