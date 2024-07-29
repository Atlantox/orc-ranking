// Creates an observer with the specified class, when the element is viewed in the navigator, the specifies class is removed

const OnAppearAnimation = (animationClass) => {
    const htmlElements = document.getElementsByClassName(animationClass)
    
    for(let i = 0; i < htmlElements.length; i++){
        const element = htmlElements[i]
        
        const myObserver = new IntersectionObserver(entries => {
            entries.forEach(entry => {
                // If the element is visible
                if (entry.isIntersecting) {
                    // Add the animation class
                    element.classList.remove(animationClass);
                }
            });
        })
        myObserver.observe(element);
    }    
}

export default OnAppearAnimation