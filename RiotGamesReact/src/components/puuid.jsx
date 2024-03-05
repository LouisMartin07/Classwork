import React, { useState, useEffect } from 'react';
import 'bootstrap/dist/css/bootstrap.min.css';


export default function PuuidFetch({ puuid }) {
  const [matchHistory, setMatchHistory] = useState([]);

  useEffect(() => {
    const fetchMatchHistory = async () => {
      const apiKey = 'RGAPI-0237f913-32f7-47f0-8a9c-3b4566abaeca';
      const region = 'americas';
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
  }, [puuid]);

  return (
    <div className="container">
      <div className="row flex-nowrap overflow-auto">
        {matchHistory.map((matchId) => (
          <div className="col-4" key={matchId}>
            <div className="card">
              <img src={`https://via.placeholder.com/800x400?text=Match+ID:+${matchId}`} className="card-img-top" alt={`Match ${matchId}`} />
              <div className="card-body">
                <h5 className="card-title">Match ID: {matchId}</h5>
                <p className="card-text">Details about Match ID: {matchId}</p>
              </div>
            </div>
          </div>
        ))}
      </div>
    </div>
  );
}



