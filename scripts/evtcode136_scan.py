from epics import caget, caput, cainfo
val = 790000
delta = 7000
import time
while 1:
    val += delta
    caput('IM3K4:PPM:CAM:EVR:TRIG4:TDES',val)
    print(caget('IM3K4:PPM:CAM:EVR:TRIG4:TDES'))
    time.sleep(5)
