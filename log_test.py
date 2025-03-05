# File Logging Test
# AMLPPC Environment Logger
# Created by: Reese Ford 03/05/2025
# Modified by: Reese Ford 03/05/2025
# Last Commit: c0c5017b232ed86b9eb7915dd879315ccce377ec

import time
import datetime
import sys
import random
import RPi.GPIO as GPIO

file_name = "test_data_log.csv"

# Setup GPIO
shutdown_pin = 36
GPIO.setmode(GPIO.BCM)
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
    
    # Log Loop
    while True:
        current_date_time = datetime.datetime.now()
        current_date_time = current_date_time.strftime("%Y%m%d %H:%M:%S.%f")
        print(current_date_time)

        temp = random.random()
        hum = random.random()

        log.write(current_date_time + "," + str(temp) + "," + str(hum) + "\n")
        
        # Shutdown Actions
        if GPIO.input(shutdown_pin) == GPIO.LOW:
            print("Shutdown Detected")
            log.close()
            sys.exit()

        time.sleep(0.5)

except KeyboardInterrupt:
    print("Recieved Keyboard Interrupt")
    log.close()
    sys.exit()