import librosa
import librosa.display
import matplotlib.pyplot as plt

filename = "XC127466"

a, sr = librosa.load("AudioSamples/"+filename+".mp3")
librosa.display.waveshow(a, sr=sr)
plt.show()
