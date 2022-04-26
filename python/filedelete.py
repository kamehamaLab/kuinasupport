from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload
from oauth2client.service_account import ServiceAccountCredentials
import os

def getGoogleService():
    scope = ['https://www.googleapis.com/auth/drive.file']
    keyFile = 'credentials.json'
    credentials = ServiceAccountCredentials.from_json_keyfile_name(keyFile, scopes=scope)
    return build("drive", "v3", credentials=credentials, cache_discovery=False)

def deletefileinGoogleDrive(deletefileID):
    service = getGoogleService()
    file = service.files().delete(fileId=deletefileID).execute()

getGoogleService()
deletefileinGoogleDrive('1NEvS-gtO2IEFaupYPJiito9DHY3lt2j_')
