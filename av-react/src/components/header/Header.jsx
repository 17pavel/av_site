import logo from '/Logo_av.by.png'
import './Header.css'
import { CarsService } from '../../service'
import { useQuery } from '@tanstack/react-query'
import { redirect } from 'react-router-dom'


export default function Header() {

    return (
        <header>
            <nav className='nav'>
                <div className='header_conteiner'>
                    <div className='header_logo'>
                        <img src={logo} className="logo" alt="logo" />
                    </div>

                </div>
                <ul className='nav_main'>
                    <li>
                        <div className='dropdown'>
                            <button className='drpdwn'>Транспорт</button>
                            <div className="dropdown-content">

                                <a href='/'>Автомобили с пробегом</a>
                                <a href='/'>Новые автомобили</a>
                                <a href='/'>Грузовой транспорт</a>
                                <a href='/'>Мототехника</a>
                                <a href='/'>Спецтехника</a>
                                

                            </div>
                        </div>
                    </li>
                    <li>
                        <div className='dropdown'>
                            <button className='drpdwn'>Запчасти и шины</button>
                            <div className="dropdown-content">
                                <a href='/'>Шины и диски</a>
                                <a href='/'>Б/у запчасти для авто</a>
                                <a href='/'>Весь авто на запчасти</a>
                                <a href='/'>Автотовары и расходники</a>
                            </div>
                        </div>
                    </li>
                    <li>
                        <a href='/'>Журнал</a>
                    </li>
                    <li>
                        <div className='dropdown'>
                            <button className='drpdwn'>Знания</button>
                            <div className="dropdown-content">
                                <a href='/'>Продажа автомобиля</a>
                                <a href='/'>Покупка автомобиля</a>
                                <a href='/'>Сделка купли-продажи</a>
                                <a href='/'>Налоги и сборы</a>
                                <a href='/'>Техосмотр</a>
                            </div>
                        </div>
                    </li>
                    <li>
                        <a href='/'>Финансы</a>
                    </li>
                    <li>
                        <div >
                            <button className='vin'>Проверка VIN</button>
                        </div>
                    </li>
                </ul>
                <ul className='nav_personal'>
                    <li>
                        <a href='/'>Войти</a>
                    </li>
                    <li>
                        <div >
                            <button className='add' >Подать объявление</button>
                        </div>
                    </li>
                </ul>
            </nav>


        </header>
    )
}
