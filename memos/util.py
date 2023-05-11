from time import mktime
from time import strptime
import mimetypes


def timeToUnix(zh):
    dt_str = zh
    dt = strptime(dt_str, '%Y-%m-%d %H:%M:%S')
    unix_ts = mktime(dt)
    ts_str = str(int(unix_ts))
    return ts_str


def getType(filename):
    file_type, _ = mimetypes.guess_type(filename)
    if file_type:
        content_type, _ = file_type.split('/')
    else:
        content_type = 'application/octet-stream'
    return content_type


