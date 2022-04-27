from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload
from oauth2client.service_account import ServiceAccountCredentials
import os

def getGoogleService(keyFile):
    scope = ['https://www.googleapis.com/auth/drive.file']
    credentials = ServiceAccountCredentials.from_json_keyfile_name(keyFile, scopes=scope)
    return build("drive", "v3", credentials=credentials, cache_discovery=False)

def deletefileinGoogleDrive(deletefileID, keyFile):
    service = getGoogleService(keyFile)
    file = service.files().delete(fileId=deletefileID).execute()
    print("Deletion Success")

def uploadFileToGoogleDrive(fileName, localFilePath, remotedirID, keyFile):
    service = getGoogleService(keyFile)
    file_metadata = {"name": fileName, "mimeType": "audio/wav", "parents": [remotedirID]}
    media = MediaFileUpload(localFilePath, mimetype="audio/wav", resumable=True)
    file = service.files().create(body=file_metadata, media_body=media, fields='id').execute()
    #print("File created, id:", file.get("id"))
    print("Upload Success")
    return (file.get("id"))
