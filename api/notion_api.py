import requests
from datetime import datetime

def query_a_databases() :
    url = "https://api.notion.com/v1/databases/869fdb1b36654418a1abf6194a0433f6/query"

    headers = {
        "Accept": "application/json",
        "Notion-Version": "2022-02-22",
        "Authorization": "Bearer secret_GAAWOZue9mvbCG8nN1IL7gS06rNZarUAnL6FOp4ZT86"
    }

    data = requests.post(url, headers=headers).json()
    pages = data['results']

    calendar_objects = []
    for p in pages :
        properties = p['properties']  #TODO treat parsing error Exception

        page = {}
        page['start_date'] = properties['Date']['date']['start']
        page['end_date'] =  properties['Date']['date']['end']
        page['name'] = properties['Name']['title'][0]['plain_text']
        page['icon'] = p['icon']

        calendar_objects.append(page)
    __list_to_map(calendar_objects)
    return calendar_objects

def __list_to_map(pages) :
    map = {}
    for page in pages :
        if (page['end_date']) : 
            diff = datetime.strptime(page['end_date'], '%Y-%m-%d') - datetime.strptime(page['start_date'], '%Y-%m-%d')
            #TODO datetime range for
            #print(diff)
            #print(type(diff)) #delta
        map[page['start_date']] = page

if __name__ == '__main__':
    query_a_databases()