import serial
import matplotlib.pyplot as plt

s = serial.Serial("/dev/cu.HC-05-DevB")
data = []

import matplotlib.animation as animation
import time
import binascii as bin

fig = plt.figure()
ax1 = fig.add_subplot(1,1,1)

print( s.readline() )

wmm = []
wmf = []
whl = []
wlf = []

def animate(i):
    global wmm, wmf, whl, wlf
    d1 = s.readline().decode('utf-8').strip()
    data.append( d1.split(';')[0].split(',') )

    mf = []
    mm = []
    hl = []
    lf = []

    for eachLine in data:
        #print( eachLine[0] )

        mf.append(int( eachLine[0] ))
        mm.append(int( eachLine[1] ))
        hl.append(int( eachLine[2] ))
        lf.append(int( eachLine[3] ))
    
    ax1.clear()

    mff = []
    lff = []
    hlf = []
    mmf = []

    for i in range( 1, len(mf)-1 ): mff.append( mf[i-1:i+2] )
    for i in range( 1, len(mm)-1 ): mmf.append( mm[i-1:i+2] )
    for i in range( 1, len(lf)-1 ): lff.append( lf[i-1:i+2] )
    for i in range( 1, len(hl)-1 ): hlf.append( hl[i-1:i+2] )

    wmf = [ sum(x)/3.0 for x in mff ]
    wmm = [ sum(x)/3.0 for x in mmf ]
    whl = [ sum(x)/3.0 for x in hlf ]
    wlf = [ sum(x)/3.0 for x in lff ]

    start = len(wmf) - 100
    end   = len(wmf)

    plt.axis( [start, end, 0, 1024] )

    ax1.plot(wmf, label='MF')
    ax1.plot(wmm, label='MM')
    ax1.plot(whl, label='HL')
    ax1.plot(wlf, label='LF')

    plt.ylabel("Pressure (Relative Resistance)")
    plt.xlabel("Time (Ticks)")
    plt.title("Pressure vs Time")    
    ax1.legend(bbox_to_anchor=(1, 1), bbox_transform=plt.gcf().transFigure)

try:
    ani = animation.FuncAnimation(fig, animate, interval=15)
    plt.show()    
finally:
    #print(wmf)
    fd = open("out.txt", "w")

    fd.write("out.txt")
    fd.write("\nMF\n")
    for i in wmf: fd.write("%d," % i)

    fd.write("\nMM\n")
    for i in wmm: fd.write("%d," % i)

    fd.write("\nLF\n")
    for i in wlf: fd.write("%d," % i)

    fd.write("\nHL\n")
    for i in whl: fd.write("%d," % i)

