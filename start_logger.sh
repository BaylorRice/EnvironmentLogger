#!/bin/sh
# start_logger.sh
# Navigate to home directory, then this directory, then execute python script

cd /
cd /home/pi/Documents/TempLogger
sudo python enviro_logger.py >> output.log 2>&1
