async function fetchPokemonPic() {
    const pokemonName = document.getElementById('pokemonName').value;
    const url = `https://pokeapi.co/api/v2/${pokemonName}`;

    try {
        const response = await fetch(url);
        const data = await response.json();
        displayPokemonPic(data);//not data, swap it out
    } catch (error) {
        document.getElementById('pokemonPic').innerText = 'Failed to load Pokemon information.';
    }
}

function displayPokemonPic(data) { //not data, swap it out
    const infoDiv = document.getElementById('Pokemonpic');
    infoDiv.innerHTML = `
        <p>Summoner Name: ${data.name}</p>
        <p>Summoner Level: ${data.summonerLevel}</p>
        <p>Account ID: ${data.accountId}</p>
    `;
}
