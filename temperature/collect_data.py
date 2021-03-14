# Read data from the Waveshare BME280 sensor on a Raspberry Pi.

import smbus2
import bme280
import requests
import time

# set i2c port, address
port = 1
address = 0x77

# set bus
bus = smbus2.SMBus(port)

try:
    # set calibration parameters
    calibration_parameters = bme280.load_calibration_params(bus, address)
except:
    pass

# read key.txt to get the key for the Flint node
with open('key.txt') as f:
    key = f.read().strip()

while True:
    # take a reading, return a compensated_reading object
    data = bme280.sample(bus, address, calibration_parameters)
    
    # convert temperature to fahrenheit
    temperature = (int(data.temperature) * 1.8) + 32
    temperature = int(temperature)
    
    # save the timestamp
    timestamp = data.timestamp
    
    # create a temperature entry
    url = 'http://ec2-18-218-173-23.us-east-2.compute.amazonaws.com/temperature/writetemp/1/' + str(temperature)
    
    # send the temperature entry
    dict = {'key':str(key)}
    requests.post(url, dict)

    # wait for one minute, then run the loop again
    time.sleep(60)
