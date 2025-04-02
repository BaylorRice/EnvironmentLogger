# EnvironmentLogger
Environment Logger for DHT22 (Senior Design)

## Circuit Diagram
![Image of the circuit diagram of the environment logger. The DHT22 is plugged into GPIO4, and the button is pulled-down and plugged into GPIO26](https://github.com/user-attachments/assets/4c5fbeab-9ffd-4231-b6e5-af0a74767131)

This assumes that the Raspberry Pi is setup already.
New Pi setup coming soon(tm)

## To Start
1. Plug in the Raspberry Pi's USBc cable
2. That's it. It's logging the temperature and humidity every few seconds.

## To Stop
1. Press and hold the button until the fan stops, and the green led stops blinking and turns off.
2. Unplug the USBc cable from the Pi

## To Download Data Log
1. Plug in the Raspberry Pi's USBc cable
2. Connect your computer to the Raspberry Pi with an Ethernet cable
3. SSH into the Pi using the provided credentials
4. Run the "kill_logger.sh" script to stop the logger (starts running on startup).
5. Download the log to your local computer using SCP or a program like Visual Studio

For help, contact reese_ford1@baylor.edu, the owner of this repository.
