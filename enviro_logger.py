# Environment Logger Script
# AMLPPC Environment Logger
# Created by: Reese Ford 03/17/2025
# Modified by: Reese Ford 03/19/2025
# Last Commit: af3bd5cdc8c9868588be0295921087ed6086c350

import time
import datetime
import sys
import random
import RPi.GPIO as GPIO
import os
import adafruit_dht
import board
import subprocess

# Setup Shutdown GPIO
shutdown_pin = 26 #Board Pin 37
GPIO.setmode(GPIO.BCM)
GPIO.setup(shutdown_pin, GPIO.IN)

file_name = "data_log.csv"
dht_pin = board.D4
dht_device = adafruit_dht.DHT22(dht_pin)

def read_temp_hum():
    temp_c = None
    hum = None

    try:
        temp_c = dht_device.temperature
        hum = dht_device.humidity
    except RuntimeError as error:
        print(error.args[0])

    if temp_c is None:
        temp_c = "ERROR"
    else:
        print("Temp = {}*C".format(temp_c))

    if hum is None:
        hum = "ERROR"
    else:
        print("Hum = {}%".format(hum))

    return temp_c, hum

def is_ntp_synced():
    try:
        result = subprocess.run(["timedatectl","show"], capture_output=True, text=True, check=True)
        output = result.stdout
        for line in output.split("\n"):
            if "NTPSynchronized=yes" in line:
                return True
    except subprocess.CalledProcessError as e:
        print("Error executing timedatectl:", e)
    return False

# Open log file
try:
    log = open(file_name, "x")
    write_header = True
except:
    print("File Already Exists")
    write_header = False
    log = open(file_name, "a")

try:
    # Write Header if new file
    if write_header:
        log.write("DateTime,Temperature (*C),Humidity (%)\n")
    else:
        log.write("START,---,---\n")
    
    # Log Loop
    timesynced = False
    timesync_failcount = 0
    while True:
        current_date_time = datetime.datetime.now()
        current_date_time = current_date_time.strftime("%Y%m%d %H:%M:%S.%f")
        print(current_date_time)
        if not timesynced and is_ntp_synced() is True:
            timesynced = True
        else:
            timesync_failcount = timesync_failcount + 1
            print("Timesync failed:",timesync_failcount)

        if timesync_failcount == 5:
            print("Timesync failed. Restarting service")
            os.system("sudo systemctl restart systemd-timesyncd")
            timesync_failcount = 0

        temp = "ERROR"
        hum = "ERROR"

        data = read_temp_hum()
        temp = data[0]
        hum = data[1]

        if timesynced:
            log.write(current_date_time + "," + str(temp) + "," + str(hum) + "\n")
        else:
            log.write(current_date_time + "*," + str(temp) + "," + str(hum) + "\n")

        # Shutdown Actions
        if GPIO.input(shutdown_pin) == GPIO.HIGH:
            print("Shutdown Detected")
            log.write("STOP,---,---\n")
            log.close()
            os.system("sudo shutdown -h now")
            sys.exit()

        time.sleep(5)

except KeyboardInterrupt:
    print("Recieved Keyboard Interrupt")
    log.write("INT,---,---\n")
    log.close()
    sys.exit()