from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload
from oauth2client.service_account import ServiceAccountCredentials
import os

def uploadFileToGoogleDrive(fileName, localFilePath):
    service = getGoogleService()
    # "parents": ["****"]この部分はGoogle Driveに作成したフォルダのURLの後ろ側の文字列に置き換えてください。
    file_metadata = {"name": fileName, "mimeType": "audio/mpeg", "parents": ["1ohXp1eD2onXEhNzhk19WefYaaQenYQJF"]}
    media = MediaFileUpload(localFilePath, mimetype="audio/mpeg", resumable=True)
    file = service.files().create(body=file_metadata, media_body=media, fields='id').execute()
    print("File created, id:", file.get("id"))

def getGoogleService():
    scope = ['https://www.googleapis.com/auth/drive.file']
    keyFile = 'credentials.json'
    credentials = ServiceAccountCredentials.from_json_keyfile_name(keyFile, scopes=scope)
    return build("drive", "v3", credentials=credentials, cache_discovery=False)


getGoogleService()
uploadFileToGoogleDrive("hoge.mp3", "D:/development/kuinasupport/python/test.mp3")
