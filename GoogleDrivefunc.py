# https://console.cloud.google.com/getting-started

from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload, MediaIoBaseDownload
from oauth2client.service_account import ServiceAccountCredentials
from oauth2client import file, client, tools
from httplib2 import Http
import os
import io

#MP3:mimeType="audio/mpeg"
#WAV:mimeType="audio/wav"

def getGoogleService(keyFile):
    SCOPES = ['https://www.googleapis.com/auth/drive']
    store = file.Storage('token.json')
    creds = store.get()
    if not creds or creds.invalid:
        flow = client.flow_from_clientsecrets(keyFile, SCOPES)
        creds = tools.run_flow(flow, store)
    return build('drive', 'v3', http=creds.authorize(Http()))

def deletefileinGoogleDrive(deletefileID, keyFile):
    service = getGoogleService(keyFile)
    file = service.files().delete(fileId=deletefileID).execute()
    #print("Deletion Success")

def uploadFileToGoogleDrive(fileName, localFilePath, updirID, keyFile):
    service = getGoogleService(keyFile)
    file_metadata = {"name": fileName, "mimeType": "audio/wav", 'parents': [updirID]}
    media = MediaFileUpload(localFilePath, mimetype="audio/wav", resumable=True)
    file = service.files().create(body=file_metadata, media_body=media, fields='id').execute()
    #print("File created, id:", file.get("id"))
    #print("Upload Success")
    return (file.get("id"))

def getlistGoogleDrive(keyFile, updirID):
    service = getGoogleService(keyFile)
    list = service.files().list(q="'"+ updirID + "' in parents", fields="files(id, name)", pageSize=10, orderBy="name,modifiedByMeTime").execute()
    return (list)

def downloadtoGoogleDrive(downloadfileID, downloadfileName, savedir, keyFile):
    service = getGoogleService(keyFile)
    request = service.files().get_media(fileId=downloadfileID)
    fh = io.BytesIO()
    downloader = MediaIoBaseDownload(fd=fh, request=request)
    done = False
    while not done:
        status, done = downloader.next_chunk()
    with open(savedir+downloadfileName, 'wb') as f:
        f.write(fh.getbuffer())
        f.close()
