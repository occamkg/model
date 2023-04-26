import sys
import math
import numpy as np

def calcWingAngle(freq, min, max, time):
    return (min-max)/2*math.sin(2*math.pi*freq*time)-(min+max)/2

def calcAOA(freq, min, max, time):
    return (min-max)/2*math.cos(2*math.pi*freq*time)-(min+max)/2

def rampTo(start, end, duration, time):
    return ((start-end)/2)*(math.cos(math.pi*time/duration)-1)+start

def calcAtWbfWaAoa(wbf, meanWA, WAAmp, meanAOA, AOAAmp, time):
    minWA = meanWA - abs(WAAmp) #deg
    maxWA = meanWA + abs(WAAmp) #deg

    minAOA = meanAOA - abs(AOAAmp) #deg
    maxAOA = meanAOA + abs(AOAAmp) #deg

    wa = calcWingAngle(wbf, minWA, maxWA, time)
    aoa = calcAOA(wbf, minAOA, maxAOA, time)
    return ((0, 0, 0), (wa, 0, aoa))

def testData(vel, angle, time):
    return ((vel * time, 0, 0), (0, 0, angle))

def writeTestFile(vel, angle):
    start = 0 #s
    end = 5 #s
    dt = 0.001 #s
    # ramp = 0.2 #s
    numPoints = int((end - start) / dt + 1)

    fl = open("6DoFL.dat", "w")
    fr = open("6DoFR.dat", "w")
    fl.write("{0}\n(\n".format(numPoints))
    fr.write("{0}\n(\n".format(numPoints))
    times = np.linspace(start, end, numPoints, endpoint=True)

    # startState = testData(vel, angle, 0)
    for time in times:
        # if time < ramp:
        #     lData = [[0, 0, 0], [0, 0, 0]]
        #     for i in range(2):
        #         for j in range(3):
        #             lData[i][j] = rampTo(0, startState[i][j], ramp, time)
        #     lData = (tuple(lData[0]), tuple(lData[1]))
        # else:
        lData = testData(vel, angle, time)

        rData = ((lData[0][0], lData[0][1], lData[0][2]), (-lData[1][0], lData[1][1], lData[1][2]))

        fl.write("({0:.5f} {1})\n".format(time, str(lData).replace(',', '')))
        fr.write("({0:.5f} {1})\n".format(time, str(rData).replace(',', '')))
    fl.write(")")
    fr.write(")")
    fl.close()
    fr.close()

def writeFile(wbf, meanWA, WAAmp, meanAOA, AOAAmp):
    start = 0 #s
    end = 5 #s
    dt = 0.001 #s
    # ramp = 0.2 #s
    numPoints = int((end - start) / dt + 1)

    fl = open("6DoFL.dat", "w")
    fr = open("6DoFR.dat", "w")
    fl.write("{0}\n(\n".format(numPoints))
    fr.write("{0}\n(\n".format(numPoints))
    times = np.linspace(start, end, numPoints, endpoint=True)

    # startState = calcAtWbfWaAoa(wbf, meanWA, WAAmp, meanAOA, AOAAmp, 0)
    for time in times:
        # if time < ramp:
        #     lData = [[0, 0, 0], [0, 0, 0]]
        #     for i in range(2):
        #         for j in range(3):
        #             lData[i][j] = rampTo(0, startState[i][j], ramp, time)
        #     lData = (tuple(lData[0]), tuple(lData[1]))
        # else:
        lData = calcAtWbfWaAoa(wbf, meanWA, WAAmp, meanAOA, AOAAmp, time)

        rData = ((lData[0][0], lData[0][1], lData[0][2]), (-lData[1][0], lData[1][1], lData[1][2]))

        fl.write("({0:.3f} {1})\n".format(time, str(lData).replace(',', '')))
        fr.write("({0:.3f} {1})\n".format(time, str(rData).replace(',', '')))
    fl.write(")")
    fr.write(")")
    fl.close()
    fr.close()

if __name__ == "__main__":
    if len(sys.argv) == 6:
        writeFile(float(sys.argv[1]), float(sys.argv[2]), float(sys.argv[3]), float(sys.argv[4]), float(sys.argv[5]))
    if len(sys.argv) == 4:
        writeFile(float(sys.argv[1]), 0, float(sys.argv[2]), float(sys.argv[3]), 15)
    elif len(sys.argv) == 3:
        writeTestFile(float(sys.argv[1]), float(sys.argv[2]))
    elif len(sys.argv) == 2:
        writeTestFile(float(sys.argv[1]), 90)
    elif len(sys.argv) == 1:
        writeTestFile(0, 90)