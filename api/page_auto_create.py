from datetime import datetime
from notion.client import *
from notion.block import *

# Log-in
MY_TOKEN = 'c797d5c19ec2a1bcb5f854cea46a1775e06f5271d0bdbbe86271e92fc68bfef878ce433103e03fcdf7d874822cf48b015ed5b12f9ccf78096a08046cc9b07f0c08e02ff5bea7bcbdb305c65b5650'
PAGE_URL = 'https://www.notion.so/to-do-bc082a2ec41c405b93b6c2a7010cf4ef'
COLLECTION_ID = '35a36f72a8b34c0a86b9659b0c0e0514'

# Main
if __name__ == '__main__':
    client = NotionClient(token_v2=MY_TOKEN)
    page = client.get_block(PAGE_URL)

    # 제목 조회
    print("페이지 제목", page.title)

    # Page 생성
    #for i in range(10):
    #    print(page.children.add_new(PageBlock, title=('Code'+str(i+1).zfill(3))))

    # 데이터베이스 불러오기
    #collection = client.get_collection(COLLECTION_ID) # get an existing collection
    #cvb = page.children.add_new(PageBlock, title="TIL", collection=collection)
    
    # 뷰 타입 추가
    # view = cvb.views.add_new(view_type="table")

    #데이터베이스 뷰 보기
    cv = client.get_collection_view("https://www.notion.so/35a36f72a8b34c0a86b9659b0c0e0514?v=323805135007416bb56c78e198e709b4")
    print(cv);

    # 각 페이지마다 Code block 추가
    for child in page.children:
        child_page = client.get_block(child.id)
        new_child = child_page.children.add_new(CodeBlock)
        new_child.language="C"