// Get screen dimemsions to decide how elements are rendered
const width = window.screen.width;
const height = window.screen.height;


// run animation as soon as possible
// Only loop 50 times to save browser resources in case of inactive user

// words to loop in animation
const words = ['Developer.', 'Engineer.', 'Programmer.', 'Enthusiast.']
let loopCount = 0;

// recursice function to erase word till there's no letter left
//afterwards, call write word with the next viable count and increment the loop counter to track loop
const eraseWord = (index_of_words, i) => {
    const wordErased = i;
    const word = words[index_of_words];
    const title = document.getElementById('title');
    setTimeout(() => {
        title.innerHTML = (word.slice(0, word.length - i));
        i++
        if (i < word.length + 1) {

            eraseWord(index_of_words, i);
        }
        else {
            loopCount++;
            if (loopCount < 50) {
                index_of_words < 3 ? writeWord(index_of_words + 1, 0) : writeWord(0, 0);
            }
            else {
                title.innerHTML = 'Developer.'
            }

        }
    }, 100);

}


// write words function
// recursive function to write words till there's none left. If left, erase
const writeWord = (index_of_words, i) => {
    let word = words[index_of_words]
    const title = document.getElementById('title');
    let count = i || 0;

    title.innerHTML = word.slice(0, i)

    count++;
    setTimeout(() => {
        if (count < word.length + 1) {
            writeWord(index_of_words, count);
        }
        else {
            eraseWord(index_of_words, 0);
        }
    }, 200)

}


// erase words function


const alertOfRender = () => {
    alert("Note: Most of my projects are hosted on free services, which occasionally put sites to sleep to conserve power. As a result, it may take up to 50 seconds for the server to wake up and load the site or show an error incase of pythonanywhere. If the site isn't loading properly, please try reloading the page. Thank you for your understanding.")
}

const hideRepertoire = () => {
    const repertoire = document.getElementById('repertoire');

    repertoire.classList.add('hiderepertoireclass')
    setTimeout(() => {
        repertoire.style.display = 'none';
        repertoire.classList.remove('hiderepertoireclass')
    }, 1000)


}

const showRepertoire = () => {
    const repertoire = document.getElementById('repertoire');
    repertoire.style.height = 0 + 'vh';
    repertoire.style.display = 'block';
    repertoire.classList.add('showrepertoireclass')
    setTimeout(() => {
        repertoire.classList.remove('showrepertoireclass')
        repertoire.style.height = 100 + 'vh';

    }, 1000);
}

// make sure window has loaded before trying to render DOM
window.onload = function () {
        // run first immeidatly dom loads.

        // remode the class that hides the word "Software"
        document.getElementById('software').classList.remove('hide-soft');
        // start animating remaining part of sentence via loop
        writeWord(0, 0);


    //background image setting
    const backgroundImg = document.getElementById('back');
    backgroundImg.style.width = width + 'px';
    backgroundImg.style.height = height + 'px';

    // container for full app 
    const container = document.getElementById('full-container');
    container.style.width = width + 'px'


    //main container
    const mainContainer = document.getElementById('main');
    //mainContainer.style.width = width < 601 ? (80/100 * width) + 'px' : width < 1025 ? (60/100 * width) +'px': (50/100 * width) +'px';

    //main head
    const mainHead = document.getElementById('main-head');
    mainHead.style.fontSize = (width / 15) + 'px';
    mainHead.style.width = width < 601 ? (80 / 100 * width) + 'px' : width < 1025 ? (60 / 100 * width) + 'px' : (50 / 100 * width) + 'px';

    //pfp
    const pfp = document.getElementById('pfp');
    const val = width < 601 ? width / 4 : width > 601 && width < 1025 ? width / 5 : width / 8
    pfp.style.width = val + 'px';
    pfp.style.height = val + 'px';
    pfp.style.borderRadius = val + 'px';


}

