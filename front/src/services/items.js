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

    getById(id) {
      // axios.defaults.headers.common['Authorization'] = 'Token ' + token;
      return axios.get(this.baseURL  + `item/${id}`);
    }
  
    login(data){
      return axios.post("http://localhost:8000/api/login/", data);
    }   
  
    signup(data){
      return axios.post("http://localhost:8000/api/signup/", data);
    }      
  }
  
  export default new DataService();




