import librosa
import matplotlib.pyplot as plt
if __name__ == "__main__":
    wave, fs = wav_read(path_to_wavefile)
    rms = librosa.feature.rms(y=wave) #音量の計算
    times = librosa.times_like(rms, sr=fs) #時間軸の生成
    plt.plot(times, rms[0]*2**(1/2)) #rms➡振幅に変換
    plt.show()
    plt.close()
