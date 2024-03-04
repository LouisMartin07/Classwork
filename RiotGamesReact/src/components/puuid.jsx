import React, { useState, useEffect } from 'react';
import Carousel from 'react-bootstrap/Carousel';
import 'bootstrap/dist/css/bootstrap.min.css';

export default function PuuidFetch({ puuid }) {
  const [matchHistory, setMatchHistory] = useState([]);

  useEffect(() => {
    const fetchMatchHistory = async () => {
      const apiKey = 'RGAPI-0237f913-32f7-47f0-8a9c-3b4566abaeca'; 
      const region = 'americas'; // Adjust per user region
      const url = `https://${region}.api.riotgames.com/lol/match/v5/matches/by-puuid/${puuid}/ids?api_key=${apiKey}`;

      try {
        const response = await fetch(url);
        const data = await response.json();
        setMatchHistory(data); 
      } catch (error) {
        console.error('Failed to fetch match history:', error);
      }
    };

    fetchMatchHistory();
  }, [puuid]); //will this know when the puuid changes in another file? 

  return (
    <Carousel id="carouselExampleDark" className="carousel carousel-dark slide">
      {matchHistory.map((matchId, index) => (
        <Carousel.Item key={matchId} className={index === 0 ? 'active' : ''}>
          <img src={`https://via.placeholder.com/800x400?text=Match+ID:+${matchId}`} className="d-block w-100" alt={`Match ${matchId}`} />
          <div className="carousel-caption d-none d-md-block">
            <h5>Match ID: {matchId}</h5>
            <p>Details about Match ID: {matchId}</p>
          </div>
        </Carousel.Item>
      ))}
      <button className="carousel-control-next" type="button" data-bs-target="#carouselExampleDark" data-bs-slide="next">
        <span className="carousel-control-next-icon" aria-hidden="true"></span>
        <span className="visually-hidden">Next</span>
      </button>
    </Carousel>
  );
}


