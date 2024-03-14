function toggleMenu(x) {
    // Add or remove the change class to the icon
    x.classList.toggle("change");
    // Add or remove the change class to the menu
    document.querySelector(".sidebar").classList.toggle("change");
  }
  document.addEventListener("DOMContentLoaded", function () {
      animateSentences();
  });

  function animateSentences() {
      const sentences = document.querySelectorAll(".sentence");
      let index = 0;

      function displaySentence() {
          if (index < sentences.length) {
              sentences[index].style.display = "block";
              setTimeout(() => {
                  sentences[index].style.display = "none";
                  index++;
                  displaySentence();
              }, 2000); // Display each sentence for 1 second
          } else {
              index = 0; // Reset index to repeat the animation
              displaySentence();
          }
      }

      displaySentence();
  }