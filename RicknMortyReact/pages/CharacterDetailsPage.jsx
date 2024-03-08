import React, { useEffect, useState } from 'react';
import { useParams } from 'react-router-dom';
import axios from 'axios';

const CharacterDetailsPage = () => {
    const [character, setCharacter] = useState(null);
    
    const { id } = useParams();

    const getData = async () => {
        const response = await axios.get(`https://rickandmortyapi.com/api/character/${id}`);

        setCharacter(response.data);
    }

    useEffect(() => {
        getData();
            
    }, [id]);

    return (
        <>
            {character && ( //added becuase it would render nothing on page load 
                <>
                    <h1>Name: {character.name}</h1>
                    <p>Status: {character.status}</p>
                    <p>Species: {character.species}</p>
                    <p>Type: {character.type}</p>
                    <p>Gender: {character.gender}</p>
                    <p>Origin: {character.origin.name}</p>
                    <p>Location: {character.location.name}</p>
                    <img src={character.image} alt={character.name} />
                </>
            )}
        </>
    );
};

export default CharacterDetailsPage;


