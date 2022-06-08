#https://heartstat.net/2021/05/15/python_calc-volume/

import librosa
import librosa.display
import matplotlib.pyplot as plt
import numpy as np

filename = "XC127466"

y, sr = librosa.load("AudioSamples/"+filename+".mp3")

rms = librosa.feature.rms(y=y)
times = librosa.times_like(rms, sr=sr)
plt.plot(times, rms[0]*2**(1/2)) #rms➡振幅に変換
plt.show()
