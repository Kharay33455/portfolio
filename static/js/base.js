console.log('linked');
// Get screen dimemsions to decide how elements are rendered
const width = window.screen.width;
const height = window.screen.height;


// make sure window has loaded before trying to render DOM
window.onload = function () {
    //background image setting
    const backgroundImg = document.getElementById('back');
    backgroundImg.style.width = width + 'px';
    backgroundImg.style.height = height + 'px';

    // container for full app 
    const container = document.getElementById('full-container');
    container.style.height = height + 'px';
    container.style.width = width + 'px'


    //main container
    const mainContainer = document.getElementById('main');
    //mainContainer.style.width = width < 601 ? (80/100 * width) + 'px' : width < 1025 ? (60/100 * width) +'px': (50/100 * width) +'px';

    console.log('done')

    //main head
    const mainHead = document.getElementById('main-head');
    mainHead.style.fontSize = (width / 20) + 'px';
    mainHead.style.width = width < 601 ? (80 / 100 * width) + 'px' : width < 1025 ? (60 / 100 * width) + 'px' : (50 / 100 * width) + 'px';

    //pfp
    const pfp = document.getElementById('pfp');
    const val = width / 3
    pfp.style.width = val + 'px';
    pfp.style.height = val + 'px';
    pfp.style.borderRadius = val + 'px';


    // run animation last after all other resources have loaded
    // Only loop 50 times to save browser resources in case of inactive user

    // words to loop in animation
    const words = ['Developer.', 'Engineer.', 'Programmer.', 'Enthusiast.']



    // write words function
    // recursive function to write words till there's none left. If left, erase
    const writeWord = (index_of_words, i) => {
        let word = words[index_of_words]
        const title = document.getElementById('title');
        let count = i || 0;
        
        title.innerHTML = word.slice(0, i)
        console.log(count)
        console.log(word)
        count++;
        setTimeout(()=>{
            if (count < word.length +1) {
                writeWord(index_of_words, count);
            }
            else{
                //eraseWord(index_of_words);
                console.log('Done')
            }
        },200)

    }

    writeWord(2, 0);

    // erase words function

}

