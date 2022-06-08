import librosa
import librosa.display
import matplotlib.pyplot as plt
import numpy as np

filename = "XC127466"

y, sr = librosa.load("AudioSamples/"+filename+".mp3")

D = np.abs(librosa.stft(y, n_fft=2048, hop_length=512))

S = librosa.feature.melspectrogram(y=y, sr=sr)#ここでy=yみたいに明示的にパラメータ指定しないとワーニング吐く
S_DB = librosa.amplitude_to_db(S, ref=np.max)
plt.figure(figsize=(16, 6))
librosa.display.specshow(S_DB, sr=sr, hop_length=512, x_axis='time', y_axis='log')
plt.colorbar()
plt.show()
