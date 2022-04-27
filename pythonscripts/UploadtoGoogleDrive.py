# https://console.cloud.google.com/getting-started

from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload
from oauth2client.service_account import ServiceAccountCredentials
import os
import csv
from glob import glob
import time
from GoogleDrivefunc import getGoogleService, deletefileinGoogleDrive, uploadFileToGoogleDrive

remotedirID = "1ohXp1eD2onXEhNzhk19WefYaaQenYQJF" #ファイルをアップロードするフォルダの末尾のID
keyFile = "credentials.json" # ドライブに接続するためのjson設定ファイル

#あとから値を代入する変数郡
fileID = ""
fileName = ""

try:
    while True:
        files = glob("RECdatas/*.wav")
        if len(files) > 0:
            files.sort(cmp=lambda x, y: int(os.path.getctime(x) - os.path.getctime(y)))
            fileName = os.path.basename(files[0])

            getGoogleService()
            fileID = uploadFileToGoogleDrive(fileName, files[0], remotedirID)
            with open('Logs/UploadLog.csv', 'a') as f:
                writer = csv.writer(f)
                writer.writerow(filename, fileID)

        else :
            time.sleep(100)



except KeyboardInterrupt:
    print("Ctrl+C finished")
