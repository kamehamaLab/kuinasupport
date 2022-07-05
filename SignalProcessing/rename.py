import glob
import os

path = "AudioSamples/yanbarukuina/cutaudio"
files = glob.glob(path + "/*")
for i, f in enumerate(files):
    os.rename(f, os.path.join(path, 'yanbarukuina_' + str(i).zfill(3) + ".mp3"))
