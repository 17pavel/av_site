import { useEffect, useState } from "react";
import { Link } from 'react-router-dom'

import DataService  from '../services/items';
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
            setItem(response.data.results);
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
      <h1>Объявления о продаже</h1>      
        <div className={styles.carGrid}>
            {item.slice(0, visibleItems).map(item => (
            <div key={item.id} className={styles.carItem}>
                <h2>{item.name}</h2>
                {item.images && item.images.length > 0 && (
                <img src={item.images[0].image} alt={item.name} />
                )}
                <p>{item.description}</p>
                <ul>
                {Object.entries(item.parameter)
                    .filter(([key]) => ['Год', 'Марка', 'Модель'].includes(key))
                    .map(([key, value]) => (
                    <li key={key}>
                        <strong>{key}:</strong> {value}
                    </li>
                    ))}
                </ul>
                <p className={styles.price}>Price: {item.price}</p>
                <Link className={styles.btn} to={`/item/${item.id}`}>Посмотреть</Link>
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
