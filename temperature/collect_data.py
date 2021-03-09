# Read data from the Waveshare BME280 sensor on a Raspberry Pi.

import smbus2
import bme280
import requests

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

# take a reading, return a compensated_reading object
data = bme280.sample(bus, address, calibration_parameters)

# save the temperature
temperature = int(data.temperature)

# create a temperature entry
requests.get('ec2-3-139-88-44.us-east-2.compute.amazonaws.com:8000/temperature/writetemp/1/' + str(temperature))
