from downloader import DownloadBioTD
import time
import os
from setWallpaper import changeBackground

imagePath = os.getcwd() + "\\bing.jpg"
while True:
    DownloadBioTD()
    changeBackground(imagePath)
    time.sleep(86400)