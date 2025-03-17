# Environment Logger Script
# AMLPPC Environment Logger
# Created by: Reese Ford 03/17/2025
# Modified by: Reese Ford 03/17/2025
# Last Commit: ea9397f3fda27c78f1d30d1665a07620943d07c9

import time
import datetime
import sys
import random
import RPi.GPIO as GPIO
import os
import adafruit_dht
import board

file_name = "data_log.csv"
dht_pin = board.D4
dht_device = adafruit_dht.DHT22(dht_pin)

def read_temp_hum():
    try:
        temp_c = dht_device.temperature
        temp_f = temp_c * (9 / 5) + 32
        hum = dht_device.humidity
        print("Temp = {1:.1f}*F Hum = {}%".format(temp_f, hum))
        return temp_c, hum

    except RuntimeError as error:
        print(error.args[0])
        return "ERROR", "ERROR"


# Setup Shutdown GPIO
shutdown_pin = 37
GPIO.setmode(GPIO.BOARD)
GPIO.setup(shutdown_pin, GPIO.IN)

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
    while True:
        current_date_time = datetime.datetime.now()
        current_date_time = current_date_time.strftime("%Y%m%d %H:%M:%S.%f")
        print(current_date_time)

        temp, hum = read_temp_hum()

        log.write(current_date_time + "," + str(temp) + "," + str(hum) + "\n")
        
        # Shutdown Actions
        if GPIO.input(shutdown_pin) == GPIO.HIGH:
            print("Shutdown Detected")
            log.write("STOP,---,---\n")
            log.close()
            os.system("sudo shutdown -h now")
            sys.exit()

        time.sleep(1)

except KeyboardInterrupt:
    print("Recieved Keyboard Interrupt")
    log.write("INT,---,---\n")
    log.close()
    sys.exit()