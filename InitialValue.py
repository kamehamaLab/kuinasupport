###############################
#
#汎用的に使う変数をまとめている。
#システムを動かす上で基本的には変える必要のない変数をまとめている。
#(必要があるなら変えるべき)
#変数名が長いし、全て大文字なので使うときはimportした上でローカル変数に入れ込むと良い
#例
# from InitialValue import AUDIODIRID
# AudioDirID = AUDIODIRID
#
#命名規則（なんちゃって）
#汎用変数は全て大文字
# DIR：ローカルのフォルダ変数の最後につく
# ID : GoogleDrive上のフォルダ変数の最後につく
#
##############################



#GoogleDriveに接続するための認証情報があるファイル名。Githubには載せないようにしよう
KEYFILE = "client_secret.json"

#ローカルで録音データが保存されるフォルダ名
AUDIOSAVEDIR = "RECdata/"

LOGSSAVEDIR　= "Logs/"

#録音データをアップロードするGoogleDrive上のフォルダID。そのフォルダをブラウザで開いた時のURLの末尾
AUDIOUPLOADDIRID = "1wwjo-qGYtEtJJE94_nq5R0oSd41JnFg4"

#各種ログファイルをアップロードするフォルダID。そのフォルダをブラウザで開いた時のURLの末尾
LOGSDIRID = "1s5DCX9C1IcA3p-TeeV_zPvqj2KA65ywE"

#画像アップロードフォルダのID
IMAGESDIRID = "1q6Y4Rb2wXG-Mo6LW_mH5wK9Uz43rW4ND"

# MIMEtyoe:wave
WAVEMIME = "audio/wav"

#MIMEtyoe:csv
CSVMIME = "text/csv"
