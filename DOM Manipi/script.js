function replaceImages() {
    console.log("Button clicked!"); 
 
    const images = document.getElementsByTagName('img');
    
    for (let i = 0; i < images.length; i++) {
        console.log("Alt attribute of image " + (i + 1) + ": " + images[i].alt);
    }

    const newText = document.createTextNode("This image couldn't be loaded.");
    
    for (let i = 0; i < images.length; i++) {
        const parent = images[i].parentNode;
        parent.replaceChild(newText.cloneNode(true), images[i]);
    }
}

document.getElementById('replaceButton').addEventListener('click', replaceImages);
