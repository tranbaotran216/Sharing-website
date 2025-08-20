import api from "./api"

export const listBooks = (q) =>
    api.get("/projects", { params: {q} }).then(res => res.data);

export const createBook = (payload) => 
    api.post("/projects", payload).then(res => res.data);

export const updateBook = (id, payload) =>
    api.put(`/projects/${id}`, payload).then(res => res.data);

export const deleteBook = (id) =>
    api.delete(`/projects/${id}`);

