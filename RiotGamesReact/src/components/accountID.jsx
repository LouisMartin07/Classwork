import { useState } from 'react';

export default function GetSummonerName({ setPuuid }) {
    const [summonerName, setSummonerName] = useState('');
    const [summonerInfo, setSummonerInfo] = useState(null);
    const [error, setError] = useState('');

    const fetchSummonerInfo = async () => {
        if (!summonerName.trim()) {
            setError('Please enter a summoner name.');
            return;
        }

        const apiKey = 'RGAPI-0237f913-32f7-47f0-8a9c-3b4566abaeca'; //need to update everyday
        const region = 'na1';
        const url = `https://${region}.api.riotgames.com/lol/summoner/v4/summoners/by-name/${encodeURIComponent(summonerName)}?api_key=${apiKey}`;

        try {
            const response = await fetch(url);
            if (!response.ok) {
                throw new Error('Failed to fetch summoner information.');
            }
            const data = await response.json();
            setSummonerInfo(data);
            setPuuid(data.puuid); 
            setError(''); 
        } catch (error) {
            setError(error.message || 'An error occurred while fetching data.');
            setSummonerInfo(null);
        }
    };

    return (
        <div>
            <div className="row g-2">
                <div className="col-md">
                    <div className="form-floating">
                        <input
                            type="text"
                            onChange={(e) => setSummonerName(e.target.value)}
                            className="form-control"
                            id="floatingInputGrid"
                            placeholder="Enter Summoner Name"
                            value={summonerName}
                        />
                        <label htmlFor="floatingInputGrid">Summoner Name</label>
                    </div>
                </div>
            </div>
            <button onClick={fetchSummonerInfo} type="button" className="btn btn-primary btn-sm">Fetch Summoner Info</button>
            {error && <p>{error}</p>}
            {summonerInfo && (
                <div className="py-8 px-8 max-w-sm mx-auto bg-white rounded-xl shadow-lg space-y-2 sm:py-4 sm:flex sm:items-center sm:space-y-0 sm:space-x-6">
                    <div className="text-center space-y-2 sm:text-left">
                        <p className="text-lg text-black font-semibold">{summonerInfo.name}</p>
                        <p className="text-slate-500 font-medium">Summoner Level: {summonerInfo.summonerLevel}</p>
                        <p className="text-slate-500 font-medium">PUUID: {summonerInfo.puuid}</p>
                    </div>
                </div>
            )}
        </div>
    );
}

