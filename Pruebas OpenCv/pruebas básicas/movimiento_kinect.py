import freenect
import time
ctx = freenect.init()
dev = freenect.open_device(ctx, freenect.num_devices(ctx) - 1)

while True:
    freenect.set_tilt_degs(dev, 0)
    time.sleep(1)
    for i in range(30):
        freenect.set_tilt_degs(dev, i)
        time.sleep(.1)
