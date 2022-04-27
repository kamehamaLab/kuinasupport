# kuinasupport

## pythonでの実装のときに参考にしたURL
[PythonでGoogleDriveAPIを使ってGoogle Driveにファイルを定期的にアップロードする](https://qiita.com/munaita_/items/d03b67b74868c3e4fb2d)  
[mimeTypeの参考元](https://www.tagindex.com/html5/basic/mimetype.html)  
[Google Drive API Delete Python](https://stackoverflow.com/questions/54131041/google-drive-api-delete-python)  
[Google Drive for developers Delete ](https://developers.google.com/drive/api/v2/reference/files/delete)
[Python:GoogleDriveAPIの基本的な使い方](https://zenn.dev/wtkn25/articles/python-googledriveapi-operation)

## メモ
wavファイルの名前は録音開始時間

## 環境構築
### raspi
~~~bash
sudo pip install --upgrade google-api-python-client google-auth-httplib2 google-auth-oauthlib oauth2client
~~~
### dataserver
~~~bash
sudo pip install --upgrade google-api-python-client google-auth-httplib2 google-auth-oauthlib oauth2client
~~~
