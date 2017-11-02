# qsat_adcs_testing

This is the python script for reading and calibrating the magnetometers. This script will run on a raspberry pi zero, with 2 mag3110 sensors connected to the I2C SDA and SCL pins. The script will prompt the user to select either calibration mode or testing mode. The calibration mode will calibrate for hard iron offsets, through rotating the sensor. 
