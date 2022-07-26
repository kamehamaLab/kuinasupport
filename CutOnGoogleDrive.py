from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload
from oauth2client.service_account import ServiceAccountCredentials
import os
import csv
import time
import datetime
from GoogleDrivefunc import getGoogleService, deletefileinGoogleDrive, getlistGoogleDrive, downloadtoGoogleDrive

keyFile = "client_secret.json"
savedir = "RECdata/"
updirID = "1wwjo-qGYtEtJJE94_nq5R0oSd41JnFg4"#1wwjo-qGYtEtJJE94_nq5R0oSd41JnFg4


def main():
    getGoogleService(keyFile)
    list = getlistGoogleDrive(keyFile, updirID)
    if len(list["files"]) > 0:
        fileID = list["files"][0]["id"]
        fileName = list["files"][0]["name"]
        downloadtoGoogleDrive(fileID, fileName, savedir, keyFile)

        deletefileinGoogleDrive(fileID, keyFile)
        with open('Logs/deleteLog.csv', 'a') as f:
            dt_now = datetime.datetime.now().strftime('%Y_%m_%d-%H_%M_%S')
            writer = csv.writer(f)
            writer.writerow([fileName, dt_now])

    else:
        print("wait")
        time.sleep(3000)




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
