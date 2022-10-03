from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload
from oauth2client.service_account import ServiceAccountCredentials
import os
import csv
import time
from GoogleDrivefunc import getGoogleService, uploadFileToGoogleDrive
from InitialValue import KEYFILE, LOGSSAVEDIR, LOGSDIRID, CSVMIME
import datetime

# 使用端末が処理サーバ「０」なのかデータ収集子機「１」なのか
mode = 1

def main():
    fileID = uploadFileToGoogleDrive("", filepath, updirID, keyFile, CSVMIME)
    if mode == 0:

    else if mode == 1:





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
