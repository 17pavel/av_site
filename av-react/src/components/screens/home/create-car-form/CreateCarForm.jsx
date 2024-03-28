// import { useState } from 'react'
// import styles from './CreateCarForm.module.css'
// import { useForm } from 'react-hook-form'
// import { useMutation } from '@tanstack/react-query'
// import { CarsService } from '../../../../services/car.service.js'

// const clearData = {
//     name: '',
//     price: '',
//     image: '',
// }

// const CreateCarForm = () => {

//     const [data, setData] = useState(clearData)

//     const { 
//         register,
//         reset, 
//         handleSubmit,
//         formState: { errors },
//         } = useForm({
//         mode: 'onChange',
//     })

//     const { mutate } = useMutation({
//         mutationKey: ['create car'],
//         mutationFn: data => CarsService.create(data)},
//         {onSucccess: () => {reset()}}
//     )


//     const createCar = data => {
//         mutate(...data)
//     }

//     return (
//         <form className={styles.form} action="" onSubmit={handleSubmit(createCar)}>
//             <input
//                 {...register('name', { required: true })}
//                 placeholder='Name'
//             />

//             {errors?.name?.message && (<p>Не то братан</p>)}

//             <input
//                 {...register('price', { required: true })}
//                 placeholder='Price'
//             />
//             <input
//                 {...register('image', { required: true })}
//                 placeholder='Image'
//             />
//             <button className='btn' >Опубликовать</button>
//         </form>
//     )
// }

// export default CreateCarForm