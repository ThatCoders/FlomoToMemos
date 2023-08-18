import json
import time

from memos.api import upFile, upMemo, deleteMemo
from memos.util import timeToUnix


def add():
    # 倒叙渐新插入符合时间感官
    flomoData = sorted(json.load(open("flomo/myMemos.json", encoding="UTF-8")), key=lambda k: k['time'])

    for flomo in flomoData:

        # 无内容纯图片则跳过, 按你的需要是否注释
        # if flomo['content'] == 'None':
        #     continue

        # 时间处理 本来想拿unix来当memo创建时间 但好像做不到修改时间
        # unix = timeToUnix(flomo['time'])

        # 文件处理
        resourceIdList = None
        if flomo['filePath'] != "None":
            resourceIdList = []
            for f in flomo['filePath']:
                fileObject = upFile(f)
                time.sleep(1.5)
                resourceIdList.append(fileObject['data']['id'])

        # 内容处理
        if resourceIdList is not None or flomo['content'] != "None":
            ct = datetime.strptime(flomo['time'], "%Y-%m-%d %H:%M:%S").timestamp()
            msg = "\n".join(flomo['content'])
            msgObject = upMemo(ct, msg, resourceIdList)
            time.sleep(0.5)
            print(f'已完成 {flomo["time"]}')


def delete(many):
    for i in range(many):
        deleteMemo(i)


if __name__ == '__main__':
    # delete(400)   # 删除ID小于many的memo, 删除了memo就能一键删除图片啦, 防止不满意的你!!!
    add()
