import serial
import time
import matplotlib.pyplot as plt
from numpy.fft import fftfreq
from scipy.fft import fft
import numpy as np


# aqui tengo toda la logica del arduino y de python para realizar una medicion
# Esto con el fin de que cada que se haga un post poder realizar una medicion!
def realizar_medicion():
    ser = serial.Serial("/dev/ttyACM1", 115200, timeout=0.1)
    time.sleep(2)
    t = 0
    data = []
    print("Iniciando medicion, espere un momento")
    while t < 200:
        line = ser.readline()  # read a byte
        if line:
            string = line.decode()  # convert the byte string to a unicode string
            num = int(string)  # convert the unicode string to an int
            data.append(num)
            t += 1
    print("Medicion finalizada")

    data = np.array(data)
    data_normalized = data[1:] / max(data[1:])

    transform = fft(data_normalized)
    x = fftfreq(data_normalized.size, d=0.1)

    max_frec = max(np.abs(transform[10:int(len(transform) / 2)]))
    index = np.where(np.abs(transform) == max_frec)[0]

    frec = 60 * x[index[0]]
    print(f"Su frecuencia cardiaca es: {frec}")

    ser.close()
    return frec

    # plt.plot(x[10:int(len(transform) / 2)], np.abs(transform[10:int(len(transform) / 2)]))
    # plt.show()
