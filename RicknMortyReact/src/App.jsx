import { Outlet } from "react-router-dom";
import './App.css';
import 'bootstrap/dist/css/bootstrap.min.css';
import Navbar from './components/Navbar';

export default function App() {

  return (
    <>
    <Navbar />
    <Outlet/>
    </>
  )
}


