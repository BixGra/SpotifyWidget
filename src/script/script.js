let elements = document.getElementsByClassName("info-container");
for (let i = 0; i < elements.length; i++) {
    let element = elements[i];
    if (element.scrollWidth > element.clientWidth) {
        let interval = setInterval(() => {
            element.scrollLeft += 1;
            if (element.scrollLeft >= element.scrollWidth - element.clientWidth) {
                element.scrollLeft = 0;
            }
        }, 50);
    }
}