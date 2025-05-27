// Fetch cat fact
async function getFact() {
  try {
    const response = await fetch("/get-fact");
    const data = await response.json();
    document.getElementById("cat-fact").textContent = data.fact;
    document.getElementById("fact-word-count").textContent = `Word count: ${data.length}`;
  } catch (error) {
    console.error("Failed to fetch cat fact", error);
  }
}

// Sound trigger 
function SoundOnTrig() {
  document.querySelectorAll(".sound-trig").forEach(element => {
    const soundSource = element.dataset.sound; //  Corrected: use .dataset.sound

    const playSound = () => {
      const audio = new Audio(soundSource); 
      audio.play();
    };

    // Add event listeners correctly inside the loop
    if (element.tagName === "BUTTON") {
      element.addEventListener("click", playSound);
    } else {
      element.addEventListener("mouseenter", playSound); 
    }
  });
}

// Initialize everything once DOM is ready
document.addEventListener("DOMContentLoaded", () => {
  const factButton = document.getElementById("fact-button");

  if (factButton) {
    factButton.addEventListener("click", getFact);
  } else {
    console.warn("fact-button not found in DOM");
  }

   //  Attach sound triggers after DOM is ready
  SoundOnTrig();
});
