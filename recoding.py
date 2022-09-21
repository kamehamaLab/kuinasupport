import pyaudio
import wave
import csv
import datetime
from InitialValue import AUDIOSAVEDIR

form_1 = pyaudio.paInt16 # 16-bit resolution
chans = 2 # 1 channel
samp_rate = 44100 # 44.1kHz　サンプリング周波数
chunk = 4096 # 2^12 一度に取得するデータ数
record_secs = 180 # 録音する秒数
dev_index = 1 # デバイス番号

AudioSaveDir = AUDIOSAVEDIR

if not os.path.exists('Logs'):
    os.makedirs('Logs')

if not os.path.exists('RECdata'):
    os.makedirs('RECdata')

def main():
    dt_now = datetime.datetime.now()
    wav_output_filename = (AudioSaveDir + dt_now.strftime('%Y_%m_%d-%H_%M_%S') + ".wav")


    audio = pyaudio.PyAudio() # create pyaudio instantiation
    # create pyaudio stream
    stream = audio.open(format = form_1, rate = samp_rate, channels = chans, input_device_index = dev_index,input = True, frames_per_buffer=chunk)
    #print("connected")
    while True:
        dt_now = datetime.datetime.now()
        wav_output_filename = ("RECdata/" + dt_now.strftime('%Y_%m_%d-%H_%M_%S') + ".wav")
        #print("recording")
        frames = []
        # loop through stream and append audio chunks to frame array
        for i in range(0,int((samp_rate/chunk)*record_secs)):
        	data = stream.read(chunk)
        	frames.append(data)
        stream.stop_stream()
        audio.terminate()
        #print("finished recording")

        wavefile = wave.open(wav_output_filename,'wb')
        wavefile.setnchannels(chans)
        wavefile.setsampwidth(audio.get_sample_size(form_1))
        wavefile.setframerate(samp_rate)
        wavefile.writeframes(b''.join(frames))
        wavefile.close()

        with open('Logs/RecodingLog.csv', 'a') as f:
            writer = csv.writer(f)
            writer.writerow([wav_output_filename])

    # stop the stream, close it, and terminate the pyaudio instantiation
    stream.stop_stream()
    stream.close()
    audio.terminate()


if __name__ == "__main__":
    while True:
        try:
            main()

        except KeyboardInterrupt:
            print("Ctrl+C finished")
            break

        except Exception as e:
            print("unexpected error")
            print(e)
