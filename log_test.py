# File Logging Test
# AMLPPC Environment Logger
# Created by: Reese Ford 03/05/2025
# Modified by: Reese Ford 03/05/2025
# Last Commit: 979d5a51d61096d72b3c1fd5bb79ec1093e7b8af

import time
import datetime
import sys
import random
import RPi.GPIO as GPIO
import os

file_name = "test_data_log.csv"

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
    
    # Log Loop
    while True:
        current_date_time = datetime.datetime.now()
        current_date_time = current_date_time.strftime("%Y%m%d %H:%M:%S.%f")
        print(current_date_time)

        temp = random.random()
        hum = random.random()

        log.write(current_date_time + "," + str(temp) + "," + str(hum) + "\n")
        
        # Shutdown Actions
        if GPIO.input(shutdown_pin) == GPIO.HIGH:
            print("Shutdown Detected")
            log.write("shutdown\n")
            log.close()
            os.system("sudo shutdown -h now")
            sys.exit()

        time.sleep(0.5)

except KeyboardInterrupt:
    print("Recieved Keyboard Interrupt")
    log.close()
    sys.exit()