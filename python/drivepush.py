from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
from oauth2client.service_account import ServiceAccountCredentials

JSON_FILE = "secret/service_account.json"
ID = "1ohXp1eD2onXEhNzhk19WefYaaQenYQJF"

gauth = GoogleAuth()
scope = ["https://www.googleapis.com/auth/drive"]
gauth.credentials = ServiceAccountCredentials.from_json_keyfile_name(JSON_FILE, scope)
drive = GoogleDrive(gauth)

file = drive.CreateFile({"title": "test.jpg", 'mimeType': 'image/jpeg'})
file.SetContentFile('test2.png')
file.Upload()
