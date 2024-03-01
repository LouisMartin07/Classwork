import React, { useState } from 'react';
import words from './words.json';
import './App.css';

function App() {
  const [puzzle, setPuzzle] = useState(words[Math.floor(Math.random() * words.length)]);
  const [guessedLetters, setGuessedLetters] = useState([]);

  const handleNewWord = () => {
    setPuzzle(words[Math.floor(Math.random() * words.length)]);
    setGuessedLetters([]); 
  };

  const addLetter = (letter) => {
    if (!letter || guessedLetters.includes(letter)) {
      alert('Please enter a new letter or a letter not already guessed.');
      return;
    }

    setGuessedLetters(prevLetters => [...prevLetters, letter]);
  };

  const handleChange = (e) => {
    const letter = e.target.value;
    if (letter && letter.length === 1) {
      addLetter(letter.toLowerCase());
    }
  };

  const displayPuzzle = () => {
    return puzzle
      .split('')
      .map(letter => guessedLetters.includes(letter) ? letter : '_')
      .join(' ');
  };

  const wrongLetters = () => {
    return guessedLetters.filter(letter => !puzzle.includes(letter)).join(', ');
  };

  return (
    <>
      <div>
        <button onClick={handleNewWord}>Set a new word</button>
      </div>
      <div>
        <input
          type="text"
          placeholder="Enter a new letter"
          maxLength="1"
          onChange={handleChange}
        />
      </div>
      <div>
        Puzzle: {displayPuzzle()}
      </div>
      <div>
        Wrong Letters: {wrongLetters()}
      </div>
    </>
  );
}

export default App;
