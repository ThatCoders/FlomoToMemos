import os
import requests
from memos.util import getType

# 需要修改 Host 与 Cookie.txt
Host = 'http://xxxxxx'  # 改成你的网址 结尾不要斜杠 例如: https://thatcoder.cn
# UserName = 'root'  # 登入账号
# PassWord = '123456'   # 登入密码
ApiBase = f'{Host}/api'
ApiSignIn = ApiBase + '/auth/signin'
ApiBlob = ApiBase + '/resource/blob'
ApiMemo = ApiBase + '/memo'


# def signIn():
#     cookie = requests.post(url=ApiSignIn, json={'username': UserName, 'password': PassWord}, headers=Headers)
#     cookie = f"access-token={cookie.cookies.get('access-token').strip()}"
#     with open('Cookie.txt', 'w') as f:
#         f.write(cookie)


def getCookie():
    with open('Cookie.txt', 'r') as c:
        Cookie = c.read()
    return Cookie


Headers = {
    'Cookie': getCookie(),
    'Accept': 'application/json, text/plain, */*',
    'Content-Type': 'application/json',
    'Referer': f'{Host}/auth',
    'Origin': Host
}


def upFile(filePath):
    boundary = '----ThatCoder.cn'  # 切片标识符
    fileName = filePath.split('/')[-1]
    with open("flomo/" + filePath, "rb") as f:  # 读取二进制文件内容
        file_data = f.read()
    # payload的encode()一个也不能删!!!
    payload = f'--{boundary}\r\nContent-Disposition: form-data; name="file";'.encode()
    payload += f'filename="{fileName}"\r\nContent-Type: {getType(fileName)}\r\n\r\n'.encode()
    payload += file_data
    payload += f'\r\n--{boundary}--'.encode()
    headers = Headers
    headers['Content-Length'] = str(os.path.getsize("flomo/" + filePath))
    headers['Content-Type'] = f'multipart/form-data; boundary={boundary}'
    response = requests.post(ApiBlob, headers=headers, data=payload)  # files参数上传方案 requests_toolbelt包
    return response.json()


def upMemo(msg, resourceIdList):
    headers = Headers
    data = {
        'content': msg,
        'visibility': 'PRIVATE',
    }
    if resourceIdList:
        data['resourceIdList'] = resourceIdList
    response = requests.post(ApiMemo, headers=headers, json=data)
    return response.json()


def deleteMemo(MemoId):
    return requests.delete(ApiMemo + f'/{MemoId}', headers=Headers).text
