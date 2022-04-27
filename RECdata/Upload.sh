#!/bin/sh
if [ -e *.wav  ]; then
    OLD_FILE="`pwd`/`ls -ltr *.wav | head -n 1 | awk '{print $9}'`"
    rclone copy $OLD_FILE GoogleDrive:
    echo "wavファイルのアップロード完了"
    rm $OLD_FILE
else
    echo  "wavファイルが存在しません。"
fi
