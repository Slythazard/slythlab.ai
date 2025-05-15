import '../src/assets/styles/App.css'
import Home from './pages/home/Home'
import Dashboard from './pages/dashboard/Dashboard.jsx'
import { BrowserRouter as Router, Routes, Route } from "react-router";


function App() {
  return (
    <Router>
      <Routes>
        <Route path="/" element={<Home/>}/>
        <Route path="/dashboard/:id" element={<Dashboard/>}/>
      </Routes>
    </Router>
  )
}

export default App
