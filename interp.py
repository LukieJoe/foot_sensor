fd = open("Profiles.txt")

fd.readline()

fd.readline()
mf = fd.readline().split(",")[:-1]
mf = [ int(x) for x in mf ]

fd.readline()
mm = fd.readline().split(",")[:-1]
mm = [ int(x) for x in mm ]

fd.readline()
lf = fd.readline().split(",")[:-1]
lf = [ int(x) for x in lf ]

fd.readline()
hl = fd.readline().split(",")[:-1]
hl = [ int(x) for x in hl ]

focus = input("toes? ").split(" ")
tmp = []

try:
    tmp = hl.copy() if focus[0] != "Y" else mf.copy()
    focus[1] = int(focus[1])
    focus[2] = int(focus[2])
except:
    exit(1)

# print( tmp[ focus[1]:focus[2] ] )

# find steps --> throw away last step, incomplete ??
steps = []
for i in range(focus[1], focus[2]):
    if int(tmp[i-1]) >= int(tmp[i]) and int(tmp[i]) < int(tmp[i+1]):
        # print( tmp[i-1], tmp[i], tmp[i+1] )
        steps.append(i)

MFP = []
cadence = []
for i in range(1, len(steps)):
    mma = sum( mm[ steps[i-1]:steps[i] ] ) / len( mm[ steps[i-1]:steps[i] ] )
    mfa = sum( mf[ steps[i-1]:steps[i] ] ) / len( mf[ steps[i-1]:steps[i] ] )
    lfa = sum( lf[ steps[i-1]:steps[i] ] ) / len( lf[ steps[i-1]:steps[i] ] )
    hla = sum( hl[ steps[i-1]:steps[i] ] ) / len( hl[ steps[i-1]:steps[i] ] )

    MFP.append( ( ( mma + mfa ) * 100 ) / ( mma + mfa + lfa + hla + 0.001 ) )
    cadence.append( (0.200 * (steps[i]-steps[i-1]) * 2) / 60.0 ) 

MFPA = sum(MFP) / len(MFP)
CADA = len(steps) / sum(cadence)

stride_len = 44.0
step_len = 18.0

speed = (stride_len / 12.0) * CADA

print( "MFP average over range: %.02d percent" % MFPA )
print( "Cadence average over range: %.02d step/min" % CADA )
print( "Speed is: %.02d ft/min" % speed )
print( "Step count over range: %s steps" % (len(steps)-1) )
print( "Stride length is: %s in" % stride_len )
print( "Step length is: %s in" % step_len )
print()

# normal 36-45
# in     30-35
# out    25-30
# heel   0
# toe    45+

if   MFPA <= 45 and MFPA >  35: guess = "NORMAL"
elif MFPA <= 35 and MFPA >  30: guess = "IN-TOE"
elif MFPA <= 30 and MFPA >  24: guess = "OUT-TOE"
elif MFPA >  45: guess = "TOE-ING"
elif MFPA <  14: guess = "HEEL-ING"

print( "Our gait guess: %s" % guess )


