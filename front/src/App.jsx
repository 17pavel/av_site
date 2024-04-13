import React from 'react';
import { Switch, Route, Link } from 'react-router-dom';
import 'bootstrap/dist/css/bootstrap.min.css';
import logo from './Logo_av.by.png'
import './Header.css'

import AddTodo from './components/add-todo';
import TodosList from './components/todos-list';
import Login from './components/login';
import Signup from './components/signup';
import DataService from './services/items';
import CarItem from './components/CarItem';
import CarDetail from './components/CarDetail';

function App() {
  const [user, setUser] = React.useState(localStorage.getItem('user') || null);
  const [token, setToken] = React.useState(localStorage.getItem('token') || null);
  const [error, setError] = React.useState('');

  async function login(user = null){ // default user to null
    DataService.login(user)
      .then(response =>{        
        setToken(response.data.token);     
        setUser(user.username);
        localStorage.setItem('token', response.data.token);
        localStorage.setItem('user', user.username);
        setError('');
      })
      .catch( e =>{
        console.log('login', e);
        setError(e.toString());       
      });
  }

  async function logout(){
    setToken('');
    setUser('');
    localStorage.setItem('token', '');
    localStorage.setItem('user', ''); 
  }

  async function signup(user = null){ // default user to null
    DataService.signup(user)
      .then(response =>{
        setToken(response.data.token);
        setUser(user.username);
        localStorage.setItem('token', response.data.token);
        localStorage.setItem('user', user.username);
      })
      .catch( e =>{
        console.log(e);
        setError(e.toString());
      })
  }

  
  return (
    <div className="App">
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

                                <a href='/car'>Автомобили с пробегом</a>
                                <a href='/truck'>Грузовой транспорт</a>
                                <a href='/moto'>Мототехника</a>
                                <a href='/spec'>Спецтехника</a>
                                

                            </div>
                        </div>
                    </li>
                    <li>
                        <div className='dropdown'>
                            <button className='drpdwn'>Запчасти и шины</button>
                            <div className="dropdown-content">
                                <a href='/tyres'>Шины и диски</a>
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
                        <Link className="nav-link" to={"/todos"}>Подать объявление</Link>
                            { user ? (
                                <Link className="nav-link" onClick={logout}>Logout ({user})</Link>
                            ) : (
                                <>
                                    <Link className="nav-link" to={"/login"}>Login</Link>
                                    <Link className="nav-link" to={"/signup"}>Sign Up</Link>
                                </>
                             )}
                    </li>
                </ul>
            </nav>
      
      <div className="container mt-4">
        <Switch>	
          <Route exact path={["/", "/item"]} render={(props) =>
            <CarItem {...props} token={token} endpoint ="item/"/>
          }>
          </Route>
          <Route exact path={[, "/item/:id/"]} render={(props) =>
            <CarDetail {...props}  id = ":id/"/>
          }>
          </Route>
          <Route exact path={["/car"]} render={(props) =>
            <CarItem {...props} token={token} endpoint ="car/"/>
          }>
          </Route>
          <Route exact path={["/moto"]} render={(props) =>
            <CarItem {...props} token={token} endpoint ="moto/"/>
          }>
          </Route>
          <Route exact path={["/truck"]} render={(props) =>
            <CarItem {...props} token={token} endpoint ="truck/"/>
          }>
          </Route>
          <Route exact path={["/spec"]} render={(props) =>
            <CarItem {...props} token={token} endpoint ="spec/"/>
          }>
          </Route>
          <Route exact path={["/tyres"]} render={(props) =>
            <CarItem {...props} token={token} endpoint ="tyres/"/>
          }>
          </Route>
          
          <Route exact path={["/todos"]} render={(props) =>
            <TodosList {...props} token={token} />
          }>
          </Route>
          <Route path="/todos/create" render={(props)=> 
            <AddTodo {...props} token={token} />
          }>
          </Route>
          <Route path="/todos/:id/" render={(props)=> 
            <AddTodo {...props} token={token} />
          }>
          </Route>
          <Route path="/login" render={(props)=> 
            <Login {...props} login={login} />
          }>
          </Route>
          <Route path="/signup" render={(props)=> 
            <Signup {...props} signup={signup} />
          }>
          </Route>
        </Switch>
      </div>
      
    </div>
  );
}

export default App;
