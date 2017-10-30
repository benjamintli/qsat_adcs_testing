
import smbus
import time
from func import hardCalibrate, readCalibration

# Get I2C bus
bus = smbus.SMBus(1)

# MAG3110 address, 0x0E(14)
# Select Control register, 0x10(16)
#		0x01(01)	Normal mode operation, Active mode
bus.write_byte_data(0x0E, 0x10, 0x01)

time.sleep(0.5)

# MAG3110 address, 0x0E(14)
# Read data back from 0x01(1), 6 bytes
# X-Axis MSB, X-Axis LSB, Y-Axis MSB, Y-Axis LSB, Z-Axis MSB, Z-Axis LSB

print "Magnetometer Python Script:"
print "0: Calibrate sensors"
print "1: Start testing"
select = input ("Make a selection:")

if select == 0:
	hardCalibrate()

if select == 1:
	x, y, z = readCalibration()
	print x
	print y
	print z
	f = open ('data.csv', 'w+')
	while True:
		try:
			data = bus.read_i2c_block_data(0x0E, 0x01, 6)
			# Convert the data
			xMag = data[0] * 256 + data[1]
			if xMag > 32767 :
				xMag -= 65536
			xMag = xMag - x

			yMag = data[2] * 256 + data[3]
			if yMag > 32767 :
				yMag -= 65536
			yMag = yMag - y

			zMag = data[4] * 256 + data[5]
			if zMag > 32767 :
				zMag -= 65536
			zMag = zMag - z

			f.write ("%d,%d,%d\n" %(xMag, yMag, zMag))
			time.sleep(0.1)
		except KeyboardInterrupt:
			break
	f.close()


#TODO write test data to a text file
