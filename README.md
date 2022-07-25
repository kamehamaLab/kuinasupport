# kuinasupport
[Google Cloud Platform](https://console.cloud.google.com/getting-started)

## ファイル構造
~~~
kuinasupport
|
|--Logs
|   |--deleteLog.csv
|   |--recodingLog.csv
|   |--UploadLog.csv
|--RECdatas
|   |--???.wav
|
|--CutOnGoogleDrive.py
|--GoogleDrivefunc.py
|--recoding.py
|--UploadtoGoogleDrive.py
~~~

## ソースファイルの説明
### CutOnGoogleDrive.py
dataserver上で動作する。  
ドライブ上にあるファイルをダウンロードしてドライブ上からは消す。

### recoding.py
ラズパイ上で動作する。  
音声ファイル（.wav）を保存する。  
生成されるwavファイルの名前は録音開始時間。  

### UploadtoGoogleDrive.py
ラズパイ上で動作する。  
ドライブにファイルをアップロードする。

### GoogleDrivefunc.py
GoogleDriveAPIを動かすためのモジュールが書かれている。

### tempRecive.py
arduinoで測った温度を記録する。

## pythonでの実装のときに参考にしたURL
[PythonでGoogleDriveAPIを使ってGoogle Driveにファイルを定期的にアップロードする](https://qiita.com/munaita_/items/d03b67b74868c3e4fb2d)  
[mimeTypeの参考元](https://www.tagindex.com/html5/basic/mimetype.html)  
[Google Drive API Delete Python](https://stackoverflow.com/questions/54131041/google-drive-api-delete-python)  
[Google Drive for developers Delete ](https://developers.google.com/drive/api/v2/reference/files/delete)
[Python:GoogleDriveAPIの基本的な使い方](https://zenn.dev/wtkn25/articles/python-googledriveapi-operation)


## メモ  
認証ファイルはgitには載せない
トークンの期限が切れないようにプロジェクトを本番環境にしないといけない
動作させるときはnohupコマンドでバックグラウンドで動かす

## 環境構築
### raspi
~~~bash
sudo pip install --upgrade google-api-python-client google-auth-httplib2 google-auth-oauthlib oauth2client
sudo pip3 install pyaudio
sudo apt install libportaudio0 libportaudio2 libportaudiocpp0 portaudio19-dev
~~~
### dataserver
~~~bash
sudo pip install --upgrade google-api-python-client google-auth-httplib2 google-auth-oauthlib oauth2client
~~~
