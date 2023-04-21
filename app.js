const speedSlider = document.getElementById("speed");
const angleSlider = document.getElementById("angle");
const speedValue = document.getElementById("speed-value");
const angleValue = document.getElementById("angle-value");
const autoCheckbox = document.getElementById("auto");
const sendButton = document.getElementById("send-command");

let autoSendInterval;

speedSlider.addEventListener("input", () => {
  updateValueDisplay(speedValue, speedSlider.value);
  if (autoCheckbox.checked) {
    sendCommandAutomatically();
  }
});

angleSlider.addEventListener("input", () => {
  updateValueDisplay(angleValue, angleSlider.value);
  if (autoCheckbox.checked) {
    sendCommandAutomatically();
  }
});

autoCheckbox.addEventListener("change", () => {
  if (autoCheckbox.checked) {
    sendCommandAutomatically();
  } else {
    clearInterval(autoSendInterval);
  }
});

sendButton.addEventListener("click", () => {
  sendCommand();
});

function updateValueDisplay(element, value) {
  element.textContent = value;
}

function sendCommandAutomatically() {
  clearInterval(autoSendInterval);
  autoSendInterval = setInterval(sendCommand, 200);
}

function sendCommand() {
  const speed = speedSlider.value;
  const angle = angleSlider.value;

  try {
    const response = fetch("http://192.168.32.129:5000/api/control", {
      method: "POST",
      headers: {
        "Content-Type": "application/json"
      },
      body: JSON.stringify({
        speed: speed,
        angle: angle
      })
    });

    if (response.ok) {
      console.log("Command sent successfully.");
    } else {
      console.error("Error sending command:", response.status);
    }
  } catch (error) {
    console.error("Error sending command:", error);
  }
}

// Initialize value displays
updateValueDisplay(speedValue, speedSlider.value);
updateValueDisplay(angleValue, angleSlider.value);

