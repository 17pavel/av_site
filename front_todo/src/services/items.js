import axios from 'axios'

class DataService{

    constructor() {
        this.baseURL = 'http://localhost:8000/api/';
    }

    getAll(token, endpoint) {
        axios.defaults.headers.common['Authorization'] = 'Token ' + token;
        return axios.get(this.baseURL + endpoint);
    }

    search(token, endpoint, query) {
        axios.defaults.headers.common['Authorization'] = 'Token ' + token;
        return axios.get(this.baseURL + endpoint, { params: { query } });
    }



    
    getCar(token){      
      axios.defaults.headers.common["Authorization"] = "Token " + token;      
      return axios.get('http://localhost:8000/api/car/');
    } 

    getMoto(token){      
      axios.defaults.headers.common["Authorization"] = "Token " + token;      
      return axios.get('http://localhost:8000/api/moto/');
    } 

    getTruck(token){      
      axios.defaults.headers.common["Authorization"] = "Token " + token;      
      return axios.get('http://localhost:8000/api/truck/');
    } 

    getSpec(token){      
      axios.defaults.headers.common["Authorization"] = "Token " + token;      
      return axios.get('http://localhost:8000/api/spec/');
    } 
  
    createTodo(data, token){
      axios.defaults.headers.common["Authorization"] = "Token " + token;
      return axios.post("http://localhost:8000/api/todos/", data);
    }
     
  
    login(data){
      return axios.post("http://localhost:8000/api/login/", data);
    }   
  
    signup(data){
      return axios.post("http://localhost:8000/api/signup/", data);
    }      
  }
  
  export default new DataService();

// export const CarsService = {
//     async getAll() {
//         const response = await axios.get('http://localhost:8000/api/item/')

//     return response.data.results
//     },

//     async getById(id) {
//         const response = await axios.get(`http://localhost:8000/api/item/${id}`)

//         return response.data
//     },

//     async getImageById(id) {
//         const response = await axios.get(`http://localhost:8000/api/image/${id}`)

//         return response.data
//     },

//     async getMainCategory() {
//         const response = await axios.get('http://localhost:8000/api/category/')

//         return response.data
//     },

//     async createItem(data, token) {
//         axios.defaults.headers.common["Authorization"] = "Token " + token;
//         return axios.post("http://localhost:8000/api/todos/", data);
//     },
       
//     async  updateItem(id, data, token){
//         axios.defaults.headers.common["Authorization"] = "Token " + token;
//         return axios.put(`http://localhost:8000/api/todos/${id}`, data);
//     },
    
//     async  deleteItem(id, token){
//         axios.defaults.headers.common["Authorization"] = "Token " + token;
//         return axios.delete(`http://localhost:8000/api/todos/${id}`);
//     },

//     async login(data){
//         return axios.post("http://localhost:8000/api/login/", data);
//     },  
    
//     async signup(data){
//         return axios.post("http://localhost:8000/api/signup/", data);
//     }   

// }




