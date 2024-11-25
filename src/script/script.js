function sleep(ms) {
    return new Promise(resolve => setTimeout(resolve, ms));
}

let elements = document.getElementsByClassName("info-container");
for (let i = 0; i < elements.length; i++) {
    let element = elements[i];
    if (element.scrollWidth > element.clientWidth) {

        let interval = setInterval(async () => {
            element.scrollLeft += 1;
            if (element.scrollLeft >= element.scrollWidth - element.clientWidth) {
                await sleep(3000);
                element.scrollLeft = 0;
                await sleep(3000);
            }
        }, 50);
    }
}