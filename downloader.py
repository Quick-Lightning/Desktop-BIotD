import subprocess, sys   
def DownloadBioTD(): 
    p = subprocess.Popen('powershell.exe -ExecutionPolicy RemoteSigned -file "downloader.ps1"', stdout=sys.stdout)
    p.communicate()