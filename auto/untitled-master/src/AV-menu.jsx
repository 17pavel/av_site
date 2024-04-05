import './App.css';
import React from 'react';
export default function AVMenu() {
    return (<div className='Av-header-line'>
        <a href=''>
            <img className='Av-logo' src='https://autobuy.by/template/autobuy/assets/icon/account/menu.svg'/>
        </a>
        <ul className='list'>
            <li>
                <a href='/'>Автомобили</a>
            </li>
            <li>
                <a href=''>Велосипеды</a>
            </li>
            <li>
                <a href=''>Компании</a>
            </li>
            <li>
                <a href=''>Автоновости</a>
            </li>
            <li>
                <a href=''>Дилерам</a>
            </li>
            <li>
                <a href=''>Продать авто</a>
            </li>
            <li>
                <a href=''>Лизинг</a>
            </li>
        </ul>
    </div>);
}