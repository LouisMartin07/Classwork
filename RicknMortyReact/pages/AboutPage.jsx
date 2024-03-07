import React from 'react';
import './AboutPage.css';

const WavyText = ({ text }) => (
  <div className="wavy-text">
    {text.split('').map((letter, index) => (
      <span key={index} style={{ '--i': index }}>{letter}</span>
    ))}
  </div>
);

const AboutPage = () => {
  const openYoutubeVideo = () => {
    window.open('https://www.youtube.com/watch?v=EBYsx1QWF9A', '_blank');
  };

  return (
    <div className="text-center p-4 bg-dark text-white" id="aboutpgcontainer">
      <h1><WavyText text="Welcome to the Rick n Morty encyclopedia" /></h1>
      <button className="btn btn-primary" onClick={openYoutubeVideo}>Explore the Multiverse</button>
    </div>
  );
};

export default AboutPage;

