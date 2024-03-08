import React from 'react';
import { useOutletContext } from 'react-router-dom';
import { Card, Button, Row, Col } from 'react-bootstrap';

const FavoritesPage = () => {
  const { favorites, removeFromFavorites } = useOutletContext();

  return (
    <Row xs={1} md={4} className="g-4">
      {favorites.map((character) => (
        <Col key={character.id}>
          <Card style={{ width: '18rem' }}>
            <Card.Img variant="top" src={character.image} />
            <Card.Body>
              <Card.Title>{character.name}</Card.Title>
              <Card.Text>
                Status: {character.status}
              </Card.Text>
              <Button variant="danger" onClick={() => removeFromFavorites(character.id)}>Remove from favorites</Button>
            </Card.Body>
          </Card>
        </Col>
      ))}
    </Row>
  );
};

export default FavoritesPage;
