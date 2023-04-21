# Getting Started 

This brief user guide will help you set up and run our application quickly and easily. Please follow the steps outlined below to ensure a smooth experience.

## Step 1: Set up the environment

Before running the application, you need to set up the environment. To do this, execute the following command:

```bash
source /opt/ros/humble/setup.py
```

## Step 2: Start the backend server

Next, navigate to the backend directory in your terminal, and run the server.py file using Python 3:

```bash
pip3 install Flask Flask-Cors 
cd backend
python3 server.py
```

# Step 3: Open the frontend in your web browser

Finally, navigate to the root directory of the application, where you will find the index.html file. Double-click on this file to open it in your default web browser.

Or visit https://gpt.w0x7ce.eu/ROS/

Our application allows you to control the speed and direction of a simulated object using the AWSD keys on your keyboard. 