from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload
from oauth2client.service_account import ServiceAccountCredentials
import os
from GoogleDrivefunc import getGoogleService, uploadFileToGoogleDrive
from InitialValue import KEYFILE, AUDIOSAVEDIR, AUDIOUPLOADDIRID
