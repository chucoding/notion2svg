from datetime import datetime
from notion.client import *
from notion.block import *
import sys, os
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

from logMng import logMng

logger = logMng().get_logger(__file__)

# Log-in
_MY_TOKEN = '85144be2363ca44777b845cd973afc35a88119e304049f248bc5e7c91aa3111bebc091040426080d2f108636c3c944a22d048264e0b1ea90446ea98c5a6e9741fab34bd2531ea4be21c159f961a0'
_PAGE_URL = 'https://www.notion.so/notion-api-test-eb72e919f19042fe99d4f1587856b4e5'

# Example
def Example01():
    client = NotionClient(token_v2=_MY_TOKEN)
    page = client.get_block(_PAGE_URL)

    # Page 생성
    for i in range(10):
        print(page.children.add_new(PageBlock, title=('Code'+str(i+1).zfill(3))))

    # 각 페이지마다 Code block 추가
    for child in page.children:
        child_page = client.get_block(child.id)
        new_child = child_page.children.add_new(CodeBlock)
        new_child.language="C"

# Main
if __name__ == '__main__':
    import requests

    headers = {
        "Accept": "application/json",
        "Notion-Version": "2022-02-22",
        "Content-Type": "application/json"
    }

    logger.info('test'*2)
    # logger.debug('request...')
    # response = requests.request("POST", _PAGE_URL, headers=headers)
    # logger.debug(response.text)
