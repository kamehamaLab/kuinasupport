import os
import csv

def yes_no_input():
    while True:
        choice = input("Initialize Logs. OK? Please respond with 'yes' or 'no' [y/N]: ").lower()
        if choice in ['y', 'ye', 'yes']:
            return True
        elif choice in ['n', 'no']:
            return False


def main():
    if not os.path.exists('token.json'):
        print("Please prepare a certification file.")
        break

    if not os.path.exists('Logs'):
        os.makedirs('Logs')
    print("Make Logs Dir")

    if not os.path.exists('RECdata'):
        os.makedirs('RECdata')
    print("Make RECdata Dir")

    if not os.path.exists('Logs/DeleteLog.csv'):
        with open('Logs/DeleteLog.csv', 'w') as f:
            writer = csv.writer(f)
            writer.writerow(["filename", "datetime"])
    print("Make Logs/DeleteLog.csv")

    if not os.path.exists('Logs/RecodingLog.csv'):
        with open('Logs/RecodingLog.csv', 'w') as f:
            writer = csv.writer(f)
            writer.writerow(["filename"])
    print("Make Logs/RecodingLog.csv")

    if not os.path.exists('Logs/TempLog.csv'):
        with open('Logs/TempLog.csv', 'w') as f:
            writer = csv.writer(f)
            writer.writerow(["datetime", "temp"])
    print("Make Logs/TempLog.csv")

    if not os.path.exists('Logs/UploadLog.csv'):
        with open('Logs/UploadLog.csv', 'w') as f:
            writer = csv.writer(f)
            writer.writerow(["filename", "fileID", "datetime"])
    print("Make Logs/UploadLog.csv")




if __name__ == '__main__':
    if yes_no_input():
        print("Initialize Logs...")
        main()
        print("Completed")

    else :
        print("Look forward to trying again!")
