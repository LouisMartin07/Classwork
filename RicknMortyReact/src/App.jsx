import { useState } from 'react'
import { Outlet } from 'react-router-dom'
import './App.css'
import RickAndMortyAttentionGetter from '../pages/HomePage'
import 'bootstrap/dist/css/bootstrap.min.css';
import Navbar from './Components/Navbar';


export default function App() {

  return (
    <>
      <div>
      <Navbar />
      </div>
      <RickAndMortyAttentionGetter />
    </>
  )
}


