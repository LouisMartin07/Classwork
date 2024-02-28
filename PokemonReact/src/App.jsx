import { useState } from 'react'
import reactLogo from './assets/react.svg'
import viteLogo from '/vite.svg'
import './App.css'
import axios from 'axios';

function App() {
  const [inputValue, setInputValue] = useState('');
  const [pokemon, setPokemon] = useState(null);
  const [pokemonTeam, setPokemonTeam] = useState([]);

  const fetchPokemonByIdOrName = async () => {
    const response = await axios.get(`https://pokeapi.co/api/v2/pokemon/${inputValue.toLowerCase()}`);
    processPokemonData(response.data);
  };

  const fetchRandomPokemon = async () => {
    const randomId = Math.floor(Math.random() * 151) + 1;
    const response = await axios.get(`https://pokeapi.co/api/v2/pokemon/${randomId}`);
    processPokemonData(response.data);
  };

  const processPokemonData = async (pokemonData) => {
    const pokemonTypeUrl = pokemonData.types[0].type.url;
    const urlResponse = await axios.get(pokemonTypeUrl);
    const pokemonOfType = urlResponse.data.pokemon.slice(0, 5).map(p => p.pokemon);

    const pokemonTeamData = await Promise.all(
      pokemonOfType.map(p => axios.get(p.url).then(res => res.data))
    );

    setPokemon(pokemonData);
    setPokemonTeam(pokemonTeamData);
  };

  return (
    <div className="pokemon-team">
      <input
        type="text"
        value={inputValue}
        onChange={(e) => setInputValue(e.target.value)}
        placeholder="Enter Pokemon ID or Name"
      />
      <button onClick={fetchPokemonByIdOrName}>Fetch Pokemon</button>
      <button onClick={fetchRandomPokemon}>Fetch Random Pokemon</button>
      <div id="pokemon-container">
        {pokemon && (
          <div>
            <h2>{pokemon.name}</h2>
            <img src={pokemon.sprites.front_default} alt={pokemon.name} />
            <p>{pokemon.types[0].type.name}</p>
          </div>
        )}
        {pokemonTeam.map((p, index) => (
          <div key={index}>
            <h2>{p.name}</h2>
            <img src={p.sprites.front_default} alt={p.name} />
            <p>{p.types[0].type.name}</p>
          </div>
        ))}
      </div>
    </div>
  );
}




export default App
