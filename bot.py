from ppadb.client import Client
import numpy as np
from mss import mss




if __name__ == "__main__":
    adb = Client()
    devices = adb.devices()

    if len(devices) == 0:
        print("Device non trovato")
        quit()

    device = devices[-1]



    tane = [
        [{'left': 100, 'top': 500, 'width': 1, 'height': 1}, [240, 1000], 1],
        [{'left': 250, 'top': 500, 'width': 1, 'height': 1}, [540, 1000], 2],
        [{'left': 370, 'top': 500, 'width': 1, 'height': 1}, [840, 1000], 3],
        [{'left': 100, 'top': 620, 'width': 1, 'height': 1}, [240, 1200], 4],
        [{'left': 250, 'top': 620, 'width': 1, 'height': 1}, [540, 1200], 5],
        [{'left': 370, 'top': 620, 'width': 1, 'height': 1}, [840, 1200], 6],
        [{'left': 100, 'top': 720, 'width': 1, 'height': 1}, [240, 1450], 7],
        [{'left': 250, 'top': 720, 'width': 1, 'height': 1}, [540, 1450], 8],
        [{'left': 370, 'top': 720, 'width': 1, 'height': 1}, [840, 1450], 9],
    ]

    int = [143, 161, 210, 255]
    ok = [160, 195, 235, 255]

    sct = mss()
    spam = []
    q = 0
    max = 50
    while True:
        if len(spam) != 0:
            if q != max:
                device.shell('input tap %s %s' % (spam[0], spam[1]))
                q += 1
        for tana in tane:
            col = np.array(sct.grab(tana[0]))[0][0]
            val1 = (col - int).sum()
            if (abs(val1) <= 20):
                device.shell('input tap %s %s' % (tana[1][0], tana[1][1]))
                print(tana[2])
                spam = tana[1]
            else :
                val2 = (col - ok).sum()
                if (abs(val2) <= 20):
                    device.shell('input tap %s %s' % (tana[1][0], tana[1][1]))
                    print(tana[2])



