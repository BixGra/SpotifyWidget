function autoScrollText(elementId) {
  const element = document.getElementById(elementId);

  // Check if the text content is wider than the container
  if (element.scrollWidth > element.clientWidth) {
    // Set up automatic scrolling
    const intervalId = setInterval(() => {
      element.scrollLeft += 1; // Adjust the scroll increment as needed

      // Stop scrolling when the end of the text is reached
      if (element.scrollLeft >= element.scrollWidth - element.clientWidth) {
        clearInterval(intervalId);
      }
    }, 10); // Adjust the interval time as needed
  }
}

autoScrollText("song")