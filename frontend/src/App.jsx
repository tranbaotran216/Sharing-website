import { BrowserRouter, Routes, Route, Link } from "react-router-dom"
import BooksPage from "./pages/BooksPage"

function Home() {
  return (
    <div style={{ padding: 16 }}>
      <h1>BookShare</h1>
      <p>Chia sẻ Books & Projects.</p>
      <Link to="/books">Đi tới Books</Link>
    </div>
  );
}

export default function App() {
  return (
    <BrowserRouter>
      <nav style={{ padding: 12, borderBottom: "1px solid #eee" }}>
        <Link to="/" style={{ marginRight: 12 }}>Home</Link>
        <Link to="/books">Books</Link>
      </nav>
      <Routes>
        <Route path="/" element={<Home/>} />
        <Route path="/books" element={<BooksPage/>} />
      </Routes>
    </BrowserRouter>
  );
}