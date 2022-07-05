##このプログラムの実行には、ffmpegをインストールする必要があります。
import glob
import numpy as np
import scipy.io.wavfile
import scipy.signal
from levinson_durbin import autocorr, LevinsonDurbin
import librosa.display
import matplotlib.pyplot as plt
from scipy.signal import find_peaks
import os

#以下のstr(””)を変える。
# 候補は”yanbarukuina”,"hato","akasyoubin","hiyodori","karasu","noguchigera","ookonohazuku","uguisu"
animal = str("hato")

mp3_dir ='./dataset/' + animal + '/cutaudio/*.mp3'
print(mp3_dir)
out_DIR = './Formant/' + animal + '/'

if not os.path.exists(out_DIR):#ディレクトリがなかったら
    os.mkdir(out_DIR)#作成したいフォルダ名を作成

mp3_list = glob.glob(mp3_dir)
file_num = len(mp3_list)
print(file_num)

def preEmphasis(signal, p):
    """プリエンファシスフィルタ"""
    # 係数 (1.0, -p) のFIRフィルタを作成
    return scipy.signal.lfilter([1.0, -p], 1, signal)

for i in range(file_num):
    #mp3ファイルのロード
    dir_path2 = R"C:\Users\hkame\Documents\bird_recog\wav"
    file_name2 = "\yanbaru.wav"
    data_clip, fs = librosa.load(mp3_list[i], sr=None, mono = False)

    data_clip_L = np.asfortranarray(data_clip[1]) #ステレオで左側の音だけを取得
    t=np.arange(0.0,len(data_clip_L)/fs,1/fs)

    # 音声波形の中心部分を切り出す
    center = len(data_clip_L) / 2  # 中心のサンプル番号
    cuttime = 0.04         # 切り出す長さ [s]
    cs = int(center - (cuttime/2)*fs)
    ce = int(center + (cuttime/2)*fs)
    s = data_clip_L[cs:ce]

    # プリエンファシスフィルタをかける
    p = 0.97         # プリエンファシス係数
    s = preEmphasis(s, p)

    # ハミング窓をかける
    hammingWindow = np.hamming(len(s))
    s = s * hammingWindow

    # LPC係数を求める
    lpcOrder = 32
    r = autocorr(s, lpcOrder + 1)
    a, e  = LevinsonDurbin(r, lpcOrder)
    #print ("*** result ***")
    #print ("a:", a)
    #print ("e:", e)

    # LPC係数の振幅スペクトルを求める
    nfft = 2048   # FFTのサンプル数
    nfft2b = int(nfft/2)

    fscale = np.fft.fftfreq(nfft, d = 1.0 / fs)[:nfft2b]

    # オリジナル信号の対数スペクトル
    spec = np.abs(np.fft.fft(s, nfft))
    logspec = 20 * np.log10(spec)
    plt.plot(fscale, logspec[:nfft2b])

    # LPC対数スペクトル
    w, h = scipy.signal.freqz(np.sqrt(e), a, nfft, "whole")
    lpcspec = np.abs(h)
    loglpcspec = 20 * np.log10(lpcspec)
    plt.plot(fscale, loglpcspec[:nfft2b], "r", linewidth=2)

    xf = fscale
    ydb =  loglpcspec[:nfft2b]

    plt.xlim(0, fs/2)
    plt.show()

    #ピークを検出
    peaks, _ = find_peaks(ydb,distance=50)

    #プロット
    fig, ax = plt.subplots(1,1,figsize=(8,6))
    fig.patch.set_facecolor('w')  # 図全体の背景色

    ax.plot(xf, logspec[:nfft2b],label='LPC')
    ax.plot(xf,ydb,color='r',lw=2,label='formant')
    ax.plot(xf[peaks], ydb[peaks], "x",mec='red',ms=10,label='f1-f10')

    # 枠の色
    ax.spines['left'].set_color('black')
    ax.spines['bottom'].set_color('black')
    # ラベルの色
    ax.xaxis.label.set_color('black')
    ax.yaxis.label.set_color('black')
    # 目盛りの色
    ax.tick_params(axis='x', colors='black')
    ax.tick_params(axis='y', colors='black')

    ax.set_xlabel("Frequency [Hz]", fontsize=20)
    ax.set_ylabel("log spectrum", fontsize=20)
    ax.tick_params(labelsize=18)
    ax.legend()

    plt.savefig(out_DIR+"/"+ animal + str(i).zfill(3) +".png")
    plt.close()

    print(str(i) + "finished")
