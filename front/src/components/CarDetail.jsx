import { Link, useParams } from "react-router-dom"
import { useState, useEffect } from "react"

import DataService  from '../services/items';
import styles from '../Home.module.css';

const CarDetail = (props) => {
  const { id } = useParams() 
  const [car, setCar] = useState([]);
  const [image, setImage] = useState([]);

  useEffect(() => {
    retrieveItem();
  }, [props.token]);

  const retrieveItem = () => {
    DataService.getById(id)
      .then((response) => {
          setCar(response.data);
          if (response.data.images) {
            const links = response.data.images.map(imageObj => imageObj.image);
            setImage(links);
        }
      })
      
      .catch((error) => {
        console.log(error);
      });

    };

    return (
        <div>
            
            <Link to={"/"}>Back</Link>
        
                <div className={styles.info}>
                    <h2>{car.name}</h2>
                    <p><b>{car.price}$</b></p>
                    <Link className={styles.btn} to={`/car/${car.id}`}>Купить</Link>
                    <ul>
                        {car.parameter && Object.entries(car.parameter).map(([key, value]) => (
                            <li key={key}>{key}: {value}</li>
                        ))}
                    </ul>
                </div>
                <div className={styles.carGrid}>
                    {image && Array.isArray(image) && image.map((image, index) => (
                        <img key={index} src={image} alt={`Image ${index}`} />
                ))}
                </div>
        </div>
    )
}

export default CarDetail