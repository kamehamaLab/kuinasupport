# https://console.cloud.google.com/getting-started

from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload
from oauth2client.service_account import ServiceAccountCredentials
import os
import csv
import time
from GoogleDrivefunc import getGoogleService, deletefileinGoogleDrive, uploadFileToGoogleDrive

remotedirID = "1ohXp1eD2onXEhNzhk19WefYaaQenYQJF" #ファイルをアップロードするフォルダの末尾のID
keyFile = "credentials.json" # ドライブに接続するためのjson設定ファイル
dirname = "RECdatas/"

#あとから値を代入する変数郡
fileID = ""
fileName = ""

try:
    while True:
        files = os.listdir(dirname)
        if len(files) > 0:
            files.sort()
            filepath = dirname + files[0]

            getGoogleService()
            fileID = uploadFileToGoogleDrive(files[0], filepath, remotedirID)
            with open('Logs/UploadLog.csv', 'a') as f:
                writer = csv.writer(f)
                writer.writerow(files[0], fileID)
            os.remove(filepath)
        else :
            time.sleep(100)



except KeyboardInterrupt:
    print("Ctrl+C finished")
