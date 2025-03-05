# DHT22 Reading Test
# AMLPPC Environment Logger
# Created by: Reese Ford 03/05/2025
# Modified by: Reese Ford 03/05/2025
# Last Commit: n/a

# Python Environment DHT22: source dht22/bin/activate

import time
import adafruit_dht
import board
import sys

dht_pin = board.D4

dht_device = adafruit_dht.DHT22(dht_pin)
try:
    while True:
        try:
            temp_c = dht_device.temperature
            temp_f = temp_c * (9 / 5) + 32
            hum = dht_device.humidity
            print("Temp = {1:.1f}*F Hum = {}%".format(temp_f, hum))

        except RuntimeError as error:
            print(error.args[0])

        time.sleep(0.2)

except KeyboardInterrupt:
    print("Recieved Keyboard Interrupt")
    sys.exit()