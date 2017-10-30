import smbus
import time
import array

def hardCalibrate ():
    sampleLength = 100 #shoot for 15 seconds of sampling
    mX = []
    mY = []
    mZ = []
    bus = smbus.SMBus(1)
    bus.write_byte_data (0x0E, 0x10, 0x01)
    for x in range(0, sampleLength):
        time.sleep (0.1)
        data = bus.read_i2c_block_data(0x0E, 0x01, 6)
        xMag = data[0] * 256 + data[1]
        if xMag > 32767 :
            xMag -= 65536
        mX.append (xMag)

        yMag = data[2] * 256 + data[3]
        if yMag > 32767 :
            yMag -= 65536
        mY.append (yMag)

        zMag = data[4] * 256 + data[5]
        if zMag > 32767 :
            zMag -= 65536
        mZ.append (zMag)


    xBias = (max(mX) + min(mX))/2
    yBias = (max(mY) + min (mY))/2
    zBias = (max(mZ) + min (mZ))/2
    print "%d,%d,%d" %(xBias, yBias, zBias)
    f = open ('calibrate.txt', 'w+')
    f.write ("%d,%d,%d" %(xBias, yBias, zBias))
    f.close()
    return;

def readCalibration ():
    c = open ('calibrate.txt', 'r')
    data = c.read().split(',')
    d = [int(e) for e in data]
    x, y ,z = d
    return x, y, z;





#TODO write calibration data to file, read calibration from file
