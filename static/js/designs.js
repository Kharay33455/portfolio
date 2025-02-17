// TO DO





const expandCenter = (entries, observer) => {
    function isIncenter(entry) {
        const demacator = window.innerWidth / 3;
        const boundary = entry.boundingClientRect.x
        console.log(demacator)
        console.log(boundary)
        if (demacator - demacator/2.5 < boundary && boundary <  demacator + demacator/2.5) {
            return true;
        } else {
            return false;
        }

    };

    entries.forEach(entry => {

        if (isIncenter(entry) === true) {
            entry.target.children[0].classList.add('expand');
            entry.target.classList.add('expand');
        } else {
            try {
                entry.target.children[0].classList.remove('expand');
                entry.target.classList.remove('expand');
            } catch (error) {
                
            }

        }
        observer.unobserve(entry.target);
    });
}

const observer = new IntersectionObserver(expandCenter, {
    root: null,
    rootMargin: '300px 300px',
    threshold: 0.1
});


const runObserver = () => {
    const listOfPages = Array.from(document.getElementsByClassName('singlePage'));
    for (let i = 0; i < listOfPages.length; i++) {
        listOfPages[i].classList.add(i);
        observer.observe(listOfPages[i]);
    }
}



window.onload = () => {
    runObserver();
    document.getElementById('carCont').addEventListener('scroll', runObserver);

}