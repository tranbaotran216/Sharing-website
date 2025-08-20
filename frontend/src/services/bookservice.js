import api from "./api"

export const listBooks = (q) =>
    api.get("/books", { params: {q} }).then(res => res.data);

export const createBook = (payload) => 
    api.post("/books", payload).then(res => res.data);

export const updateBook = (id, payload) =>
    api.put(`/books/${id}`, payload).then(res => res.data);

export const deleteBook = (id) =>
    api.delete(`/books/${id}`);

