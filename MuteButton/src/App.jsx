import { useState } from 'react'
import offLogo from '/off.svg'
import onLogo from '/on.svg'
import './App.css'

function App() {
  const [image, setImage] = useState(onLogo)

  const toggleImage = () => {
    setImage(currentImage => currentImage === onLogo? offLogo : onLogo);
  }

  return (
    <>
      <h1> Huge Mute Button</h1>
      <div>
        <button onClick={toggleImage}>
          <img src={image} alt="Toggle Button" />
        </button>
      </div>

    </>
  )
}

export default App
