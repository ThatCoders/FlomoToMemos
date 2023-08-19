from time import mktime
from time import strptime
import mimetypes


def timeToUnix(zh):
    dt_str = zh
    dt = strptime(dt_str, '%Y-%m-%d %H:%M:%S')
    unix_ts = mktime(dt)
    ts_str = str(int(unix_ts))
    return ts_str


def getType(file_ext):
    file_type = ''
    if file_ext == ".jpg" or file_ext == ".jpeg":
        file_type = 'image/jpeg'
    elif file_ext == ".png":
        file_type = 'image/png'
    elif file_ext == ".mp3" or file_ext == ".wav":
        file_type = 'audio/mpeg'
    elif file_ext == ".doc" or file_ext == ".docx":
        file_type = 'application/msword'
    elif file_ext == ".pdf":
        file_type = 'application/pdf'
    elif file_ext == ".txt":
        file_type = 'text/plain'
    elif file_ext == ".xls" or file_ext == ".xlsx":
        file_type = 'application/vnd.ms-excel'
    elif file_ext == ".ppt" or file_ext == ".pptx":
        file_type = 'application/vnd.ms-powerpoint'
    elif file_ext == ".xml":
        file_type = 'text/xml'
    elif file_ext == ".zip":
        file_type = 'application/zip'
    elif file_ext == ".apk":
        file_type = 'application/vnd.android.package-archive'
    elif file_ext == ".exe":
        file_type = 'application/octet-stream'
    elif file_ext == ".js":
        file_type = 'text/javascript'
    elif file_ext == ".css":
        file_type = 'text/css'
    elif file_ext == ".html":
        file_type = 'text/html'
    else:
        file_type = 'application/octet-stream'
    return file_type


