import React, { useState, useEffect } from 'react';
import axios from 'axios';
import { Card, Button, Row, Col } from 'react-bootstrap'; 

const EpisodesPage = () => {
  const [episodes, setEpisodes] = useState([]);

  useEffect(() => {
    const fetchEpisodes = async () => {
      const result = await axios('https://rickandmortyapi.com/api/episode');
      setEpisodes(result.data.results);
    };
    fetchEpisodes();
  }, []);

  return (
    <Row xs={1} md={4} className="g-4"> {/* adjust "md" for the desired number of cards per row */}
      {episodes.map((episode) => (
        <Col key={episode.id}> 
          <Card style={{ width: '18rem' }}>
            <Card.Img variant="top" src={episode.image} />
            <Card.Body>
              <Card.Title>{episode.name}</Card.Title>
              <Card.Text>
                Air date: {episode.air_date}
              </Card.Text>
              <div className="d-flex justify-content-between"> 
              <Button variant="primary" onClick={() => detailsButtonClick(character.id)}>Details</Button>
              <Button variant="primary" onClick={() => favoritesButtonClick(character.id)}>Add to favorites</Button>
              </div>
            </Card.Body>
          </Card>
        </Col>
      ))}
    </Row>
  );
};
export default EpisodesPage;

