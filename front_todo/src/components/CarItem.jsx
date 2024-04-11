import { useEffect, useState } from "react";
import { Link } from 'react-router-dom'

import DataService  from '../services/items';
// import Header from '../../header/Header.jsx';
// import { useQuery } from '@tanstack/react-query';
import styles from '../Home.module.css';

const CarItem = (props) => {
  const [item, setItem] = useState([]);
  const [visibleItems, setVisibleItems] = useState(20);

  useEffect(() => {
    retrieveItem();
  }, [props.token, props.endpoint]);

  const retrieveItem = () => {
    DataService.getAll(props.token, props.endpoint)
      .then((response) => {
        setItem(response.data);
      })
      .catch((error) => {
        console.log(error);
      });
  };

  const totalItems = item.length;

  const handleShowMore = () => {
    setVisibleItems((prevVisibleItems) => prevVisibleItems + 20);
  };

  return (
      <div>
      <h1>Объявления о продаже автомобилей с пробегом в Беларуси</h1>

      
      <div className={styles.carGrid}>
          {item.slice(0, visibleItems).map(car => (
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

export default CarItem;
