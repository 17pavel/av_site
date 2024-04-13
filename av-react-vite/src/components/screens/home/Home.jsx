import { useContext, useState } from "react";
import CarItem from './car-item/CarItem.jsx';
import { Link } from 'react-router-dom'

import { CarsService } from '../../../service.js';
import Header from '../../header/Header.jsx';
import { AuthContext } from '../../../users/AuthProvider.jsx';
import { useQuery } from '@tanstack/react-query';
import styles from './Home.module.css';

function Home() {

  // const [user, setUser] = React.useState(null);
  // const [token, setToken] = React.useState(null);
  // const [error, setError] = React.useState('');

  // async function login(user = null){ // default user to null
  //   CarsService.login(user)
  //     .then(response =>{        
  //       setToken(response.data.token);     
  //       setUser(user.username);
  //       localStorage.setItem('token', response.data.token);
  //       localStorage.setItem('user', user.username);
  //       setError('');
  //     })
  //     .catch( e =>{
  //       console.log('login', e);
  //       setError(e.toString());       
  //     });
  // }

  // async function logout(){
  //   setToken('');
  //   setUser('');
  //   localStorage.setItem('token', '');
  //   localStorage.setItem('user', ''); 
  // }

  // async function signup(user = null){ // default user to null
  //   CarsService.signup(user)
  //     .then(response =>{
  //       setToken(response.data.token);
  //       setUser(user.username);
  //       localStorage.setItem('token', response.data.token);
  //       localStorage.setItem('user', user.username);
  //     })
  //     .catch( e =>{
  //       console.log(e);
  //       setError(e.toString());
  //     })
  // }

  const { data, isLoading } = useQuery({
    queryKey: ['cars'],
    queryFn: () => CarsService.getAll()
  });

  const [visibleItems, setVisibleItems] = useState(20);

  if (isLoading) return <p>Loading...</p>;

  const totalItems = data.length;

  const handleShowMore = () => {
    setVisibleItems(prevVisibleItems => prevVisibleItems + 20);
  };

  return (
    <div>
      <Header />
      <h1>Объявления о продаже автомобилей с пробегом в Беларуси</h1>
      <div className={styles.carGrid}>
        {data.slice(0, visibleItems).map(car => (
          <div key={car.id} className={styles.carItem}>
            <h2>{car.name}</h2>
            {car.images && car.images.length > 0 && (
              <img src={car.images[0].image} alt={car.name} />
            )}
            <p>{car.description}</p>
            <ul>
              {Object.entries(car.parameter)
                .filter(([key]) => ['Год', 'Марка', 'Модель'].includes(key))
                .map(([key, value]) => (
                  <li key={key}>
                    <strong>{key}:</strong> {value}
                  </li>
                ))}
            </ul>
            <p className={styles.price}>Price: {car.price}</p>
            <Link className='btn' to={`/car/${car.id}`}>Посмотреть</Link>
          </div>
        ))}
      </div>
      <div className={styles.showMore} onClick={handleShowMore}>
        Показать еще 20
      </div>
      <p className={styles.totalCount}>
        Из: {totalItems}
      </p>
    </div>
  );
}

export default Home;