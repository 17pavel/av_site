import React, {useState} from "react";
import axios from "axios";
import  ReCAPTCHA  from "react-google-recaptcha";
import {Link} from "react-router-dom";

const API_URL ='http://127.0.0.1:8000/api/user/'

export default function Autorisation() {
    const [name, setName] = useState('')
    const [pas, setPas] = useState('')
    const [pref,setPref] = useState('29')
    const [phone,setPhone] = useState('')


    const addNewUser = async () => {
  try {
      const newUser = {name: name, phone: pref+phone, password: pas};
    const response = await axios.post(API_URL, newUser);
    return response.data
  } catch (err) {
    console.error(err.toJSON())
  }


}
const [isCaptchaSuccessful, setIsCaptchaSuccess] = React.useState(false)

  function onChange(value) {
    setIsCaptchaSuccess(true)
    console.log("captcha value: ", value);
  }
    return (
        <div className='aut'>
            <img src="https://autobuy.by/template/autobuy/assets/img/autobuyprofile.svg" alt="autobuyid" title="autobuyid"/>

            <p><strong>Введите номер телефона</strong></p>
            <p>Чтобы зарегистрироваться или войти на сайт</p>
            <div> <p>Мобильный телефон
                <span><strong> +375</strong></span>
                <select value={pref} onChange={(e) => setPref(e.target.value)}>
                    <option>29</option>
                    <option>33</option>
                    <option>44</option>
                    <option>25</option>
                </select><input value={phone} onChange={(e) => setPhone(e.target.value)}/>  </p>
            </div>
            <div>
                <p><span>Имя </span>
                <input value={name} onChange={(e) => setName(e.target.value)}/></p>
                <p><span>Пароль </span>
                <input type='password' value={pas} onChange={(e) => setPas(e.target.value)}/></p>
            </div>
            <ReCAPTCHA
          sitekey={process.env.REACT_APP_RECAPTCHA_SITE_KEY}
          onChange={onChange}

          />
            <div>
                <p></p>
                <Link to='/'><button disabled={!isCaptchaSuccessful} onClick={addNewUser}>Далее</button></Link>

            </div>

        </div>

    )
}