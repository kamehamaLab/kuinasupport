import librosa
import librosa.display
import matplotlib.pyplot as plt

filename = "XC127466"

a, sr = librosa.load("AudioSamples/"+filename+".mp3")
librosa.display.waveshow(a, sr=sr)
print(type(a)) #type:numpy.ndarray
print(type(sr)) #type:int
print( 'a length :%d' % len(a))
print('Sampling rate (Hz): %d' % sr)
print('Audio length (seconds): %.2f' % (len(a) / sr))
plt.show()
