import { useEffect, useState } from "react";
import { listBooks, createBook, deleteBook } from "../services/bookservice";

export default function BooksPage() {
    const [items, setItems ] = useState([]);
    const [q, setQ] = useState("");
    const [form, setForm] = useState({ title: "", author: "", description: "" });
    const load = async () => setItems(await listBooks(q));

    useEffect(() => { load(); }, []); //first load
    useEffect(() => { const t = setTimeout(load, 300); return () => clearTimeout(t); }, [q]); //search

    const onSubmit = async (e) => {
        e.preventDefault();
        if (!form.title.trim())  return;
        await createBook(form);
        setForm({ title: "", author: "", description: ""});
        await load();
    };

    return (
        <div style={{ maxWidth: 720, margin: "24px auto", padding: 16}}>
            <h1>Books</h1>

            <input 
                placeholder="Tìm theo tiêu đề..."
                value={q}
                onChange={(e) => setQ(e.target.value)}
                style={{ width:  "100%", padding: 8, marginBottom: 12}}
            />

            <form onSubmit={onSubmit} style={{ display: "grid", gap: 8}}>
                <input placeholder="Title *" value={form.title}
                        onChange={(e) => setForm({ ...form, title: e.target.value})}/>

                <input placeholder="Author" value={form.author}
                        onChange={(e) => setForm({ ...form, author: e.target.value})}/>

                <textarea placeholder="Description" value={form.description}
                        onChange={(e) => setForm({ ...form, description: e.target.value})}/>

                <button type="submit">Add book</button>        
            </form>

            <ul style={{ marginTop: 24 }}>
                {items.map(b => (
                    <li key= {b.id} style={{ border: "1px solid #ddd", padding: 12, marginBottom: 12 }}>
                        <b>{b.title}</b> {b.author ? `— ${b.author}` : ""}
                        <div style={{ fontSize: 14, color: "#555" }}>{b.description}</div>
                        <button onClick={async () => { await deleteBook(b.id); await load(); }}
                                style={{ marginTop: 8 }}>
                        Delete
                        </button>
                    </li>
                ))}
            </ul>
        </div>
    );
}

