const speedSlider = document.getElementById("speed");
const angleSlider = document.getElementById("angle");
const autoCheckbox = document.getElementById("auto");
const sendButton = document.getElementById("send-command");

let autoSendInterval;

speedSlider.addEventListener("input", () => {
  if (autoCheckbox.checked) {
    sendCommandAutomatically();
  }
});

angleSlider.addEventListener("input", () => {
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

function sendCommandAutomatically() {
  clearInterval(autoSendInterval);
  autoSendInterval = setInterval(sendCommand, 200);
}

async function sendCommand() {
  const speed = document.getElementById("speed").value;
  const angle = document.getElementById("angle").value;
  
  // http://your-backend-server-url/api/control
  try {
    const response = await fetch("http://127.0.0.1:5000/api/control", {
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

