function copy(elementId, buttonId, new_class) {
    let element = document.getElementById(elementId);
    navigator.clipboard.writeText(element.innerText);
    element = document.getElementById(buttonId);
    if (element.innerText === "Copy") {
        element.innerText = "Copied !";
    }
    element.setAttribute("class", new_class);
}