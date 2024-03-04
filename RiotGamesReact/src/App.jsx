import { useState } from 'react'
import GetSummonerName from './components/accountID';
import PuuidFetch from './components/puuid';
import './App.css'
import React from "react";


function App() {
  const [puuid, setPuuid] = useState(''); //needed to pass data back n forth between accountID and puuid

  return (
    <>
      <div>
        <GetSummonerName setPuuid={setPuuid} />
      </div>
      <div>
        {puuid && <PuuidFetch puuid={puuid} />}
      </div>
    </>
  );
}

export default App;
