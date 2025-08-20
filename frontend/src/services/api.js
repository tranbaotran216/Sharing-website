import axios from "axios";

const API_URL = import.meta.env.VITE_API_URL

const api = axios.create({
    baseURL: import.meta.env.API_URL || "http://localhost:8000",
});


export default api;

