import { Link, useParams } from "react-router-dom"
import { CarsService } from "../../../../service.js"
import { useState, useEffect } from "react"
import CarItem from "../car-item/CarItem.jsx"
import styles from '../Home.module.css'
import Header from "../../../header/Header.jsx"

const CarDetail = () => {

    const { id } = useParams()
    const [car, setCar] = useState({})
    const [image, setImage] = useState({})
    // const [parameter, setParameter] = useState({})
    useEffect(() => {

        if (!id) return

        const fetchDataCars = async () => {
            const data = await CarsService.getById(id)
            console.log(data)

            setCar(data)

            if (data.images) {
                const links = data.images.map(imageObj => imageObj.image);
                setImage(links);
            }
        };

        

        fetchDataCars()
    }, [id]);

    return (
        <div>
            <Header />
            <Link to='/'>Back</Link>
        
                <div className={styles.info}>
                    <h2>{car.name}</h2>
                    <p><b>{car.price}$</b></p>
                    <Link className='btn' to={`/car/${car.id}`}>Купить</Link>

                    
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