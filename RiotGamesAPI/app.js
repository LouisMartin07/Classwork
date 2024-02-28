// Riot Games API Key: RGAPI-1dc8f7b6-27fd-4696-8b4e-52bcb6837364

async function fetchSummonerInfo() {
    const summonerName = document.getElementById('summonerName').value;
    const apiKey = 'RGAPI-1dc8f7b6-27fd-4696-8b4e-52bcb6837364';
    const region = 'na1'; //adjust per user region
    const url = `https://${region}.api.riotgames.com/lol/summoner/v4/summoners/by-name/${summonerName}?api_key=${apiKey}`;

    try {
        const response = await fetch(url);
        const data = await response.json();
        displaySummonerInfo(data);
    } catch (error) {
        document.getElementById('summonerInfo').innerText = 'Failed to load summoner information.';
    }
}

function displaySummonerInfo(data) {
    const infoDiv = document.getElementById('summonerInfo');
    infoDiv.innerHTML = `
        <p>Summoner Name: ${data.name}</p>
        <p>Summoner Level: ${data.summonerLevel}</p>
        <p>Account ID: ${data.accountId}</p>
    `;
}
