from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload
from oauth2client.service_account import ServiceAccountCredentials
import os
import csv
import time
from GoogleDrivefunc import getGoogleService, deletefileinGoogleDrive, getlistGoogleDrive, downloadtoGoogleDrive

keyFile = "client_secret.json"
savedir = "RECdatas/"

try:
    while True:
        getGoogleService(keyFile)
        list = getlistGoogleDrive(keyFile)
        if len(list) > 0:
            fileID = list["files"][0]["id"]
            fileName = list["files"][0]["name"]
            downloadtoGoogleDrive(fileID, fileName, savedir, keyFile)


            deletefileinGoogleDrive(fileID, keyFile)
            with open('Logs/deleteLog.csv', 'a') as f:
                writer = csv.writer(f)
                writer.writerow([fileName])

        else:
            time.sleep(100)
            print("wait")

except KeyboardInterrupt:
    print("Ctrl+C finished")
