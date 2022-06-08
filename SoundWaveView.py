#https://algorithm.joho.info/programming/python/pydub-numpy/

# -*- coding: utf-8 -*-
from pydub import AudioSegment
import numpy as np
import matplotlib.pyplot as plt

# 音楽データの読み込み
sound = AudioSegment.from_file("AudioSamples/XC127466.mp3", "mp3")

# NumPy配列に返還
data = np.array(sound.get_array_of_samples())

# ステレオ音声から片方を抽出
x = data[::sound.channels]

# グラフ化
plt.plot(x[::10])
plt.grid()
plt.show()
