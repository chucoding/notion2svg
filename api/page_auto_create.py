from datetime import datetime
from notion.client import *
from notion.block import *
import sys, os
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

from logMng import logMng

logger = logMng().get_logger(__file__)

# Log-in
_MY_TOKEN = ''
_PAGE_URL = ''

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
    
    data = {
        'parent': { 'database_id': '3eec9f9d62fa4db2bd31d47d6c6077fe' },
        'properties': {
            'Name': {
                'title': [
                    {
                        'text': {
                            'content': 'Notion API TEST~'
                        }
                    }
                ]
            }
        }
    }
    
    

    logger.info('request...')
    response = requests.request("POST", _PAGE_URL, headers=headers, data=json.dumps(data).encode('utf8'))
    logger.info(response.text)