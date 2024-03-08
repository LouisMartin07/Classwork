import { Outlet } from "react-router-dom";
import { useState } from 'react';
import './App.css';
import 'bootstrap/dist/css/bootstrap.min.css';
import Navbar from './components/Navbar';

export default function App() {
  const [favorites, setFavorites] = useState([])

  const addToFavorites = (character) => {
    const isAlreadyFavorite = favorites.some(favorite => favorite.id === character.id);
  
    if (!isAlreadyFavorite) {
      const updatedFavorites = [...favorites, character];
      setFavorites(updatedFavorites);
    } else {
      alert("This character is already in your favorites!");
    }
  };
  

  const removeFromFavorites = (characterId) => {
    const updatedFavorites = favorites.filter(c => {

      if (c.id === characterId) {
        return false
      }

      return true
    })

    setFavorites(updatedFavorites);
  };

  const checkIsFavorite = (id) => favorites.filter(c => c.id === id).length > 0;

  console.log('favorites ', favorites)

  const contextObj = {
    favorites,
    addToFavorites,
    removeFromFavorites,
    checkIsFavorite,
    message: "hello",
  };

  return (
    <>
    <Navbar />
    <Outlet context={contextObj}/> 
    </>
  )
}


