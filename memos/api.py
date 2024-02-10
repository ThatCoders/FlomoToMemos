import os
import requests
import time
from memos.util import getType

# 需要修改 Host 与 token.txt
Host = 'https://memos.thatcoder.cn'  # 改成你的网址 结尾不要斜杠 例如: https://memos.thatcoder.cn
ApiBase = f'{Host}/api/v1'
ApiSignIn = ApiBase + '/auth/signin'
ApiBlob = ApiBase + '/resource/blob'
ApiMemo = ApiBase + '/memo'



def getCookie():
    with open('token.txt', 'r') as c:
        Cookie = c.read()
    return Cookie


Headers = {
    # 'Cookie': getCookie(),    # 0.18版本左右改为    Authorization验证
    'Accept': 'application/json, text/plain, */*',
    'Content-Type': 'application/json',
    'Referer': f'{Host}/auth',
    'Origin': Host,
    'Authorization': f'Bearer {getCookie()}'
}


def upFile(filePath):
    boundary = '----ThatCoder.cn'  # 切片标识符
    file_name, file_ext = os.path.splitext(filePath.split('/')[-1])
    # 定义默认文件名
    fileName = file_name if file_name else f'匿名文件_{int(time.time())}'
    with open("flomo/" + filePath, "rb") as f:  # 读取二进制文件内容
        file_data = f.read()
    # payload的encode()一个也不能删!!!
    payload = f'--{boundary}\r\nContent-Disposition: form-data; name="file";'.encode()
    payload += f'filename="{fileName}"\r\nContent-Type: {getType(file_ext)}\r\n\r\n'.encode()
    payload += file_data
    payload += f'\r\n--{boundary}--'.encode()
    headers = Headers
    headers['Content-Length'] = str(os.path.getsize("flomo/" + filePath))
    headers['Content-Type'] = f'multipart/form-data; boundary={boundary}'
    response = requests.post(ApiBlob, headers=headers, data=payload)  # files参数上传方案 requests_toolbelt包  有https错误添加参数verify=False
    return response.json()


def upMemo(ct, msg, resourceIdList):
    """
    memos已不接受时间参数
    """
    headers = Headers
    data = {
        'createdTs': ct,
        'updatedTs': ct,
        'content': msg,
        'visibility': 'PRIVATE',
    }
    if resourceIdList:
        data['resourceIdList'] = resourceIdList
    response = requests.post(ApiMemo, headers=headers, json=data)
    return response.json()




def deleteMemo(MemoId):
    return requests.delete(ApiMemo + f'/{MemoId}', headers=Headers).text
