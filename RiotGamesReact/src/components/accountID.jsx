import { useState } from 'react'
import PuuidFetch from './puuid';

export default function GetSummonerName({ setPuuid }) {
    const [summonerName, setSummonerName] = useState('');
    const [summonerInfo, setSummonerInfo] = useState(null);
    const [error, setError] = useState('');

    const fetchSummonerInfo = async () => {
        const apiKey = 'RGAPI-0237f913-32f7-47f0-8a9c-3b4566abaeca';
        const region = 'na1'; // Adjust per user region
        const url = `https://${region}.api.riotgames.com/lol/summoner/v4/summoners/by-name/${summonerName}?api_key=${apiKey}`;

        try {
            const response = await fetch(url);
            const data = await response.json();
            setSummonerInfo(data);
            setError('');
            setPuuid(data.puuid); //sets in App.jsx
        } catch (error) {
            setError('Failed to load summoner information.');
            setSummonerInfo(null);
        }
    };

    const handleInputChange = (event) => {
        setSummonerName(event.target.value);
    };

    const displaySummonerInfo = () => {
        if (!summonerInfo) return null;
        return (
            <div className="py-8 px-8 max-w-sm mx-auto bg-white rounded-xl shadow-lg space-y-2 sm:py-4 sm:flex sm:items-center sm:space-y-0 sm:space-x-6">
                <div className="text-center space-y-2 sm:text-left">
                    <div className="space-y-0.5">
                        <p className="text-lg text-black font-semibold">
                            {summonerInfo.name}
                        </p>
                        <p className="text-slate-500 font-medium">
                            Summoner Level: {summonerInfo.summonerLevel}
                        </p>
                        <p className="text-slate-500 font-medium">
                            PUUID: {summonerInfo.puuid}
                        </p>
                    </div>
                </div>
            </div>
        );
    };

    return (
        <>
        <PuuidFetch puuid={summonerInfo?.puuid} />
            <div>
                <div className="row g-2">
                    <div className="col-md">
                        <div className="form-floating">
                            <input
                                type="text"
                                onChange={handleInputChange}
                                className="form-control"
                                id="floatingInputGrid"
                                placeholder="Enter Summoner Name"
                                value={summonerName}
                            />
                            <label htmlFor="floatingInputGrid">Summoner Name</label>
                        </div>
                    </div>
                    <div className="col-md">
                        <div className="form-floating">
                            <select
                                className="form-select"
                                id="floatingSelectGrid"
                                defaultValue="" // Add this to manage the selected option via React state if needed 
                            > 
                                <option value="" disabled>Select Region here</option>
                                <option value="1">BR1</option>
                                <option value="2">EUN1</option>
                                <option value="3">EUW1</option>
                                <option value="4">JP1</option>
                                <option value="5">KR</option>
                                <option value="6">LA1</option>
                                <option value="7">LA2</option>
                                <option value="8">NA1</option>
                                <option value="9">OC1</option>
                                <option value="10">PH2</option>
                                <option value="11">RU</option>
                                <option value="12">SG2</option>
                                <option value="13">TH2</option>
                                <option value="14">TR1</option>
                                <option value="15">TW2</option>
                                <option value="16">VN2</option>
                            </select> 
                            <label htmlFor="floatingSelectGrid">Region</label>
                        </div>
                    </div>
                </div>
                <button onClick={fetchSummonerInfo} type="button" className="btn btn-primary btn-sm">Fetch Summoner Info</button>
                {error && <p>{error}</p>}
                {displaySummonerInfo()}
            </div>
        </>
    );
}
