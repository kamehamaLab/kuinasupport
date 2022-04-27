from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload
from oauth2client.service_account import ServiceAccountCredentials
import os

def getGoogleService(keyFile):
    scope = ['https://www.googleapis.com/auth/drive.file']
    credentials = ServiceAccountCredentials.from_json_keyfile_name(keyFile, scopes=scope)
    return build("drive", "v3", credentials=credentials, cache_discovery=False)

def deletefileinGoogleDrive(deletefileID):
    service = getGoogleService()
    file = service.files().delete(fileId=deletefileID).execute()

def uploadFileToGoogleDrive(fileName, localFilePath, remotedirID):
    service = getGoogleService()
    file_metadata = {"name": fileName, "mimeType": "audio/wav", "parents": [remotedirID]}
    media = MediaFileUpload(localFilePath, mimetype="audio/wav", resumable=True)
    file = service.files().create(body=file_metadata, media_body=media, fields='id').execute()
    #print("File created, id:", file.get("id"))
    return (file.get("id"))
