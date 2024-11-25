function copy() {
    let element = document.getElementById("copy-css");
    navigator.clipboard.writeText(element.innerText);
    element = document.getElementById("copy-button");
    element.innerText = "Copied !";
    element.setAttribute("class", "zoom-bar-button-clicked bold-text rounded");
}