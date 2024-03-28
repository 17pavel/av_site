import { Link } from 'react-router-dom'
import styles from '../Home.module.css'

const CarItem = ({car}) => {
    return (
        <div key={car.id} className={styles.item}>

            <div className={styles.info}>
                <h2>{car.name}</h2>
                <p><b>{car.price}$</b></p>
                <Link className='btn' to={`/car/${car.id}`}>Посмотреть</Link>
                
            </div>
        </div>

    );
};
export default CarItem;
