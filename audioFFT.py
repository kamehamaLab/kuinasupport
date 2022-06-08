#https://qiita.com/kotai2003/items/69638e18b6d542fb275e
#https://qiita.com/lilacs/items/a331a8933ec135f63ab1#stft


import librosa
import librosa.display
import matplotlib.pyplot as plt
import numpy as np

filename = "XC127466"

y, sr = librosa.load("AudioSamples/"+filename+".mp3")

D = np.abs(librosa.stft(y, n_fft=2048, hop_length=512)) #n_fft:STFTするときの窓の長さ(デフォルトは2048)　hop_length:窓関数の移動幅（デフォルトはn_fft/4）
print(D.shape)

plt.figure(figsize=(16, 6))
plt.plot(D)
plt.grid()
plt.show()
