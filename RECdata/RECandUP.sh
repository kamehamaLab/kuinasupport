#!/bin/sh
cycle=30
time=180

recording(){
    for i in $(seq $cycle); do
	DATE=$(date +%Y-%m-%d-%H%M%S)
	rec -c 2 -r 44.1k -b 16 /home/kame-lab/RECdata/REC$DATE.wav trim 0 $time
	uploading &
    done
}

uploading(){
    if [ -e *.wav  ]; then
    	OLD_FILE="`pwd`/`ls -ltr *.wav | head -n 1 | awk '{print $9}'`"    	
	rclone copy $OLD_FILE GoogleDrive:
    	echo "wavファイルのアップロード完了"
    	rm $OLD_FILE
    else
    	echo  "wavファイルが存在しません。"
fi
wait
}

recording & 

wait
