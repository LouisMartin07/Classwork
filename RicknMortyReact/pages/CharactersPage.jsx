import { useState, useEffect } from 'react';
import { useOutletContext, useNavigate } from 'react-router-dom';
import axios from 'axios';
import { Card, Button, Row, Col } from 'react-bootstrap';

const CharactersPage = () => {
  const [characters, setCharacters] = useState([]);
  const navigate = useNavigate()
  const { addToFavorites } = useOutletContext();

  useEffect(() => {
    const fetchCharacters = async () => {
      const result = await axios('https://rickandmortyapi.com/api/character');
      setCharacters(result.data.results);
    };
    fetchCharacters();
  }, []);

  return (
    <Row xs={1} md={4} className="g-4">
      {characters.map((character) => (
        <Col key={character.id}>
          <Card style={{ width: '18rem' }}>
            <Card.Img variant="top" src={character.image} />
            <Card.Body>
              <Card.Title>{character.name}</Card.Title>
              <Card.Text>
                Status: {character.status}
              </Card.Text>
              <div className="d-flex justify-content-between">
                <Button variant="primary" onClick={() => navigate(`/characters/${character.id}`)}>Details</Button>
                <Button variant="success" onClick={() => addToFavorites(character)}>Add to favorites</Button>
              </div>
            </Card.Body>
          </Card>
        </Col>
      ))}
    </Row>
  );
};

export default CharactersPage;

