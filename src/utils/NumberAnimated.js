// Creates an observer with the specified class, when the element is viewed in the navigator, the number will increase by 0 to the element innerHTML number
const NumberAnimated = (async (animationClass) => {
    const htmlElements = document.getElementsByClassName(animationClass)
    
    for(let i = 0; i < htmlElements.length; i++){
        const element = htmlElements[i]
        
        const myObserver = new IntersectionObserver(entries => {
            entries.forEach(async entry => {
                // If the element is visible
                if (entry.isIntersecting) {
                    // Add the animation class
                    await IncreaseNumberValue(element)
                }
            });
        })
        myObserver.observe(element);
    }    
})

async function IncreaseNumberValue(htmlElement){
    //htmlElement
}
export default NumberAnimated