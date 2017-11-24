
import smbus
import time
from func import calibrate, readCalibration
import plotly.plotly as py
import plotly.tools as tls
from plotly.graph_objs import Scatter, Layout, Figure

# Get I2C bus
bus = smbus.SMBus(1)

# MAG3110 address, 0x0E(14)
# Select Control register, 0x10(16)
#		0x01(01)	Normal mode operation, Active mode
bus.write_byte_data(0x0E, 0x10, 0x01)
bus.write_byte_data(0x0E, 0x11, 0x80)

time.sleep(0.5)

username = 'qsat'
api_key = '3FOw6AhITGPSS974ofXI'
stream_tokens = tls.get_credentials_file()['stream_ids']
token_1 = '121t37at3r'
token_2 = 'ybxtyp461h'
token_3 = 'hv7iiobmtp'
py.sign_in(username, api_key)





# MAG3110 address, 0x0E(14)
# Read data back from 0x01(1), 6 bytes
# X-Axis MSB, X-Axis LSB, Y-Axis MSB, Y-Axis LSB, Z-Axis MSB, Z-Axis LSB

print "Magnetometer Python Script:"
print "0: Calibrate sensors"
print "1: Start testing"
select = input ("Make a selection:")

if select == 0:
	calibrate()

if select == 1:
	x, y, z = readCalibration()
	print x
	print y
	print z
	f = open ('data.csv', 'w+')
	c = open ('dataUncalibrated', 'w+')

	Mxy = Scatter(
	    x=[],
	    y=[],
		name = 'Mxy',
		mode = 'markers',
	    stream=dict(
	        token=token_1,
	        maxpoints=20000
	    )
	)
	Mxz = Scatter(
	    x=[],
	    y=[],
		name = 'Mxz',
		mode = 'markers',
	    stream=dict(
	        token=token_2,
	        maxpoints=20000
	    )
	)
	Myz = Scatter(
	    x=[],
	    y=[],
		name = 'Myz',
		mode = 'markers',
	    stream=dict(
	        token=token_3,
	        maxpoints=20000
	    )
	)


	layout = Layout(
	    title='MAG3110 Streaming Data'
	)
	fig = Figure(data=[Mxy, Mxz, Myz], layout=layout)


	print py.plot(fig, filename='MAG3110 Streaming Data')
	stream1 = py.Stream(token_1)
	stream2 = py.Stream (token_2)
	stream3 = py.Stream (token_3)
	stream1.open()
	stream2.open()
	stream3.open()

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
			c.write ("%d, %d, %d\n" %(xMag + x, yMag +y, zMag + z))
			stream1.write ({'x': xMag, 'y': yMag})
			stream2.write ({'x': xMag, 'y': zMag})
			stream3.write ({'x': yMag, 'y': zMag})
			time.sleep(0.2)
		except KeyboardInterrupt:
			break
	f.close()
	stream1.close()
	stream2.close()
	stream3.close()


#TODO write test data to a text file
