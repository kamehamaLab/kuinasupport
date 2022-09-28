from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload
from oauth2client.service_account import ServiceAccountCredentials
import os
import csv
import time
from GoogleDrivefunc import getGoogleService, uploadFileToGoogleDrive
from InitialValue import KEYFILE, AUDIOSAVEDIR, AUDIOUPLOADDIRID, WAVEMIME
import datetime

if not os.path.exists('Logs'):
    os.makedirs('Logs')

def main():
    keyFile = KEYFILE
    dirname = AUDIOSAVEDIR.replace("/") #処理の関係上スラッシュを削除
    updirID = AUDIOUPLOADDIRID
    wavemime = WAVEMIME


    #あとから値を代入する変数郡
    fileID = ""
    fileName = ""
    files = os.listdir(dirname)

    if len(files) > 0:
        files.sort()
        filepath = dirname + files[0]

        getGoogleService(keyFile)
        fileID = uploadFileToGoogleDrive(files[0], filepath, updirID, keyFile, wavemime)
        dt_now = datetime.datetime.now().strftime('%Y_%m_%d-%H_%M_%S')
        with open('Logs/UploadLog.csv', 'a') as f:
            writer = csv.writer(f)
            writer.writerow([files[0], fileID, dt_now])
        os.remove(filepath)
    else :
        print("wait")
        time.sleep(600)



if __name__ == "__main__":
    while True:
        try:
            main()

        except KeyboardInterrupt:
            print("Ctrl+C finished")
            break

        except BrokenPipeError:
            print("BrokenPipeError")
            print("reconnect")

        except ConnectionResetError:
            print("ConnectionResetError")
            print("reconnect")

        except Exception as e:
            print("unexpected error")
            print(e)
