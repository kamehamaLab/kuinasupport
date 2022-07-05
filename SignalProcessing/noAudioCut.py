#https://algorithm.joho.info/programming/python/pydub-split-on-silence/


# -*- coding: utf-8 -*-
from pydub import AudioSegment
from pydub.silence import split_on_silence

filename = "XC127466"

# wavファイルのデータ取得
sound = AudioSegment.from_file("AudioSamples/"+filename+".mp3", format="mp3")

# wavデータの分割（無音部分で区切る）
chunks = split_on_silence(sound, min_silence_len=2000, silence_thresh=-40, keep_silence=600)

# 分割したデータ毎にファイルに出力
for i, chunk in enumerate(chunks):
    chunk.export("AudioSamples/" + filename + "/" + "output_" + str(i) +".mp3", format="mp3")
