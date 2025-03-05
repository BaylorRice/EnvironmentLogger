# DHT22 Reading Test
# AMLPPC Environment Logger
# Created by: Reese Ford 03/05/2025
# Modified by: Reese Ford 03/05/2025
# Last Commit: n/a

# Python Environment DHT22: source dht22/bin/activate

import sys
sys.path.append('/home/pi/Documents/Adafruit_Python_DHT')
import Adafruit_DHT

sensor = Adafruit_DHT.DHT22

pin = 4

humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)

if humidity is not None and temperature is not None:
    print('Temp = {0:0.1f}*C Hum = {1:0.1f}%'.format(temperature, humidity))
else:
    print('ERROR - Failed to get reading. Try Again!')