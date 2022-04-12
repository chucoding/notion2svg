from datetime import datetime
from notion.client import *
from notion.block import *

# Log-in
_MY_TOKEN = 'c797d5c19ec2a1bcb5f854cea46a1775e06f5271d0bdbbe86271e92fc68bfef878ce433103e03fcdf7d874822cf48b015ed5b12f9ccf78096a08046cc9b07f0c08e02ff5bea7bcbdb305c65b5650'
_PAGE_URL = 'https://www.notion.so/React-949d8011b53f4bcc806644fc814011e0'

# Main
if __name__ == '__main__':
    client = NotionClient(token_v2=_MY_TOKEN)
    page = client.get_block(_PAGE_URL)

    # 제목 조회
    print("페이지 제목", page.title)

    # Page 생성
    for i in range(10):
        print(page.children.add_new(PageBlock, title=('Code'+str(i+1).zfill(3))))

    # 각 페이지마다 Code block 추가
    for child in page.children:
        child_page = client.get_block(child.id)
        new_child = child_page.children.add_new(CodeBlock)
        new_child.language="C"