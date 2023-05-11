import re

from bs4 import BeautifulSoup
import json

# 打开文件
with open('flomo/index.html', 'r', encoding='utf-8') as f:
    content = f.read()

soup = BeautifulSoup(content, 'html.parser')
memos = soup.find_all('div', class_='memo')

data = []

for memo in memos:

    # 获取时间
    memo_data = {'time': memo.find('div', class_='time').text}

    # 获取标签
    memo_copy = memo
    tags = memo_copy.find('div', class_='content').find_all('p',
                                                            string=re.compile(
                                                                r'(?<![^\W_])(?:(?<=\s)|(?<=^))#[\S]*?(?=[\s.,;!?]|[^\w\s]|$)'))
    answer = []
    for tag in tags:
        i = re.findall(r"#\w+", tag.text)
        for j in i:
            answer.append(j)
    memo_data['tags'] = [tag.strip() for tag in answer] if answer else "None"

    # 获取内容
    content = memo.find('div', class_='content').find_all('p')
    memo_data['content'] = [c.text.strip() for c in content] if content else 'None'

    # 获取文件
    files = memo.find('div', class_='files').find_all('img')
    memo_data['filePath'] = [file['src'] for file in files] if files else "None"

    data.append(memo_data)

# 写入文件
with open('flomo/myMemos.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)
    print("生成完毕 flomo/myMemos.json")

