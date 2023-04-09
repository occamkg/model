import math
import numpy as np

def calcWingAngle(freq, min, max, time):
    return (min-max)/2*math.sin(2*math.pi*freq*time)+(min+max)/2

def calcAOA(freq, min, max, time):
    return (min-max)/2*math.cos(2*math.pi*freq*time)+(min+max)/2

def createData():
    start = 0 #s
    end = 20 #s
    dt = 0.001 #s
    numPoints = int((end - start) / dt + 1)

    minWA = -60 #deg
    maxWA = 60 #deg

    minAOA = -20 #deg
    maxAOA = 30 #deg

    wbf = 2 #hz

    fl = open("6DoFL.dat", "w")
    fr = open("6DoFR.dat", "w")
    fl.write("{0}\n(\n".format(numPoints))
    fr.write("{0}\n(\n".format(numPoints))
    times = np.linspace(start, end, numPoints, endpoint=True)
    for time in times:
        wa = calcWingAngle(wbf, minWA, maxWA, time)
        aoa = calcAOA(wbf, minAOA, maxAOA, time)
        fl.write("({0:.3f} ((0 0 0) ({1:.5f} 0 {2:.5f})))\n".format(time, wa, aoa))
        fr.write("({0:.3f} ((0 0 0) ({1:.5f} 0 {2:.5f})))\n".format(time, -wa, aoa))
    fl.write(")")
    fr.write(")")
    fl.close()
    fr.close()

if __name__ == "__main__":
    createData()