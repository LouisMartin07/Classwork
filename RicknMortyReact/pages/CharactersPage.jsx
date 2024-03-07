import React, { useState, useEffect } from 'react';
import axios from 'axios';
import { Card, Button, Row, Col } from 'react-bootstrap'; 

const CharactersPage = () => {
  const [characters, setCharacters] = useState([]);

  useEffect(() => {
    const fetchCharacters = async () => {
      const result = await axios('https://rickandmortyapi.com/api/character');
      setCharacters(result.data.results);
    };
    fetchCharacters();
  }, []);

  return (
    <Row xs={1} md={4} className="g-4"> {/* adjust "md" for the desired number of cards per row */}
      {characters.map((character) => (
        <Col key={character.id}> 
          <Card style={{ width: '18rem' }}>
            <Card.Img variant="top" src={character.image} />
            <Card.Body>
              <Card.Title>{character.name}</Card.Title>
              <Card.Text>
                Status: {character.status}
              </Card.Text>
              <Button variant="primary">Learn More</Button>
            </Card.Body>
          </Card>
        </Col>
      ))}
    </Row>
  );
};
 
export default CharactersPage;

