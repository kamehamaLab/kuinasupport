#https://algorithm.joho.info/machine-learning/python-keras-convolutional-neural-network/

import numpy as np
from tensorflow.keras.models import Sequential, model_from_json
from tensorflow.keras.layers import Dense, Dropout, Flatten, Conv2D, MaxPooling2D
from tensorflow.keras.optimizers import RMSprop
from tensorflow.keras.datasets import cifar10
from tensorflow.keras.preprocessing.image import array_to_img, img_to_array, load_img
from tensorflow.keras.utils import to_categorical
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
import scipy.io.wavfile
import scipy.signal
from levinson_durbin import autocorr, LevinsonDurbin
from scipy.signal import find_peaks
import re
import os
import pickle
import librosa

def plot_history(history, save_graph_img_path, fig_size_width, fig_size_height, lim_font_size):

    acc = history.history['accuracy']
    val_acc = history.history['val_accuracy']
    loss = history.history['loss']
    val_loss = history.history['val_loss']

    epochs = range(len(acc))

    # グラフ表示
    plt.figure(figsize=(fig_size_width, fig_size_height))
    plt.rcParams['font.family'] = 'Times New Roman'
    plt.rcParams['font.size'] = lim_font_size  # 全体のフォント
    plt.subplot(121)

    # plot accuracy values
    plt.plot(epochs, acc, color = "blue", linestyle = "solid", label = 'train acc')
    plt.plot(epochs, val_acc, color = "green", linestyle = "solid", label= 'valid acc')
    plt.title('Training and Validation acc')
    plt.grid()
    plt.legend()

    # plot loss values
    plt.subplot(122)
    plt.plot(epochs, loss, color = "red", linestyle = "solid" ,label = 'train loss')
    plt.plot(epochs, val_loss, color = "orange", linestyle = "solid" , label= 'valid loss')
    plt.title('Training and Validation loss')
    plt.legend()
    plt.grid()

    plt.savefig(save_graph_img_path)
    plt.close() # バッファ解放

def main():
    # ハイパーパラメータ
    batch_size = 5 # バッチサイズ
    num_classes = 3 # 分類クラス数(今回は3種類)
    epochs = 200      # エポック数(学習の繰り返し回数)
    dropout_rate = 0.2 # 過学習防止用：入力の20%を0にする（破棄）

    FIG_SIZE_WIDTH = 12
    FIG_SIZE_HEIGHT = 10
    FIG_FONT_SIZE = 25

    # データの保存先.なければ作成（pythonのバージョンによってはexit_okは使えない）
    CNNBufDir = "CNNBufer"
    os.makedirs(CNNBufDir, exist_ok=True)

    AudioDataDir = "AudioSamples/"

    data_x = []
    data_y = []
    num_classes = 8


    animalName = ["yanbarukuina", "hato", "akasyoubin", "hiyodori", "karasu", "noguchigera", "ookonohazuku", "uguisu"]

    for i in range(len(animalName)):
        print("start load " + animalName[i])
        for j in range(0, 111):
            audio, fs = librosa.load(AudioDataDir + animalName[i] + "/cutaudio/" + animalName[i] + "_" + str(j).zfill(3) + ".mp3")
            audio_L = np.asfortranarray(audio[1])
            t=np.arange(0.0,len(audio_L)/fs,1/fs)
            center = len(audio_L) / 2
            cuttime = 0.04
            cs = int(center - (cuttime/2)*fs)
            ce = int(center + (cuttime/2)*fs)
            s = audio_L[cs:ce]
            p = 0.97         # プリエンファシス係数
            s = preEmphasis(s, p)
            hammingWindow = np.hamming(len(s))
            s = s * hammingWindow
            lpcOrder = 32
            r = autocorr(s, lpcOrder + 1)
            a, e  = LevinsonDurbin(r, lpcOrder)
            nfft = 2048   # FFTのサンプル数
            nfft2b = int(nfft/2)
            w, h = scipy.signal.freqz(np.sqrt(e), a, nfft, "whole")
            lpcspec = np.abs(h)
            print(lpcspec)
            loglpcspec = 20 * np.log10(lpcspec)
            data_x.append(loglpcspec)#学習データを配列についか
            data_y.append(i)#学習データに対応したフラグを追加
        print("finish load " + animalName[i])


    data_x =np.asarray(data_x)
    data_y = np.asarray(data_y)

    x_train, x_test, y_train, y_test = train_test_split(data_x, data_y, test_size=0.2)

    x_train = x_train.astype('float32')
    x_test = x_test.astype('float32')
    x_train = x_train / 255.0
    x_test = x_test / 255.0

    y_train = to_categorical(y_train, num_classes)
    y_test = to_categorical(y_test, num_classes)

    x_train = x_train.reshape(710,128,431,-1)
    x_test = x_test.reshape(178,128,431,-1)

    print(x_train.shape, 'x train samples')
    print(x_test.shape, 'x test samples')
    print(y_train.shape, 'y train samples')
    print(y_test.shape, 'y test samples')

    model = Sequential()

    model.add(Conv2D(32,(4,4), padding='same', input_shape=x_train.shape[1:], activation='relu'))
    model.add(Conv2D(32,(4,4), padding='same', activation='relu'))
    model.add(MaxPooling2D(pool_size=(2, 2)))
    model.add(Dropout(dropout_rate))
    model.add(Conv2D(64,(4,4), padding='same', activation='relu'))
    model.add(Conv2D(64,(4,4), padding='same', activation='relu'))
    model.add(MaxPooling2D(pool_size=(2, 2)))
    model.add(Dropout(dropout_rate))
    model.add(Flatten())
    model.add(Dense(512, activation='relu'))
    model.add(Dropout(dropout_rate))
    model.add(Dense(num_classes, activation='softmax'))
    model.compile(loss='categorical_crossentropy', optimizer=RMSprop(), metrics=['accuracy'])

    history = model.fit(x_train, y_train, batch_size=batch_size, epochs=epochs, verbose=1, validation_split=0.1)

    score = model.evaluate(x_test, y_test, verbose=0)
    print('Test loss:', score[0])
    print('Test accuracy:', score[1])
    plot_history(history,
                save_graph_img_path = CNNBufDir + "/" + "graph_LPC.png",
                fig_size_width = FIG_SIZE_WIDTH,
                fig_size_height = FIG_SIZE_HEIGHT,
                lim_font_size = FIG_FONT_SIZE)
    open(CNNBufDir  + "model_LPC.json","w").write(model.to_json())
    model.save_weights(CNNBufDir + "/" + "weight_LPC.hdf5")
    with open(CNNBufDir + "/" + "history_LPC.json", 'wb') as f:
        pickle.dump(history.history, f)

if __name__ == '__main__':
    main()
