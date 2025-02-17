// Call back function to be run by our observer. entries param is all element the observer is currently ovserving, observer is the observer itslef
const expandCenter = (entries, observer) => {

    // function to check that elemnt is in center. entry is the elemenwt we are checking
    function isIncenter(entry) {

        // 33% of scrren width
        const demacator = window.innerWidth / 3;
        
        // starting positiiong from the left of the elem being observed
        const boundary = entry.boundingClientRect.x

        // check if elem is in middle and return answer. Observe logic.. implement better if you can
        if (demacator - demacator / 2.5 < boundary && boundary < demacator + demacator / 2.5) {
            return true;
        } else {
            return false;
        }

    };

    // loop through all elems matching 
    entries.forEach(entry => {

        // check if elemt is in center
        if (isIncenter(entry) === true) {

            // if so, add the expand classlist to the elemed and its children
            entry.target.children[0].classList.add('expand');
            entry.target.classList.add('expand');

        } else {
            // if not, try to remove incase it was centered before, would throw error if it wastn, catch error.
            try {
                entry.target.children[0].classList.remove('expand');
                entry.target.classList.remove('expand');
            } catch (error) {

            }
        }
        // after all is done, unobserve the element and wait for the next scroll.
        observer.unobserve(entry.target);
    });
}

// Observer initialization. It is initialoized to run the expandCeneter() fucntion when triggered
const observer = new IntersectionObserver(expandCenter, {
    root: null,
    rootMargin: '300px 300px',
    // element should be 100% on screen before we bother running the function
    threshold: 1
});


// This function observes all the elements in the page with class name single page and runs the call back function it comes with
const runObserver = () => {

    // get all element with name. It comes as an html collection, use the array.from mehod to generate an array from it.
    const listOfPages = Array.from(document.getElementsByClassName('singlePage'));

    // loop through them and observer all
    for (let i = 0; i < listOfPages.length; i++) {
        observer.observe(listOfPages[i]);
    }

}


// start on window load
window.onload = () => {
    // Element is hidden, now that all is laoded, show
    document.getElementById('main').style.opacity = '1';

    // run the initial observer to expand who is in middle rigfht now
    runObserver();

    // add event listener on the carousel container so whenever it is scrolled, observer is run again
    document.getElementById('carCont').addEventListener('scroll', function(){
        setTimeout(()=>{
            runObserver();
        }, 300);
    });

}