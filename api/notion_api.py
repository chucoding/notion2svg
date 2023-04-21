from datetime import datetime

import requests

import config


def query_a_databases() :
    url = f"https://api.notion.com/v1/databases/{config.db}/query"
    headers = {
        "Authorization": f"Bearer secret_{config.auth}",
        "Accept": "application/json",
        "Notion-Version": "2022-02-22",
    }

    data = {
        "filter": {
            "property": "Date",
            "date": {
                "after":"2023-04-01"
                }
            }
    }
    res = requests.post(url, data, headers=headers).json()
    print(res)
    pages = res['results']

    calendar_objects = []
    for p in pages :
        properties = p['properties']  #TODO treat parsing error Exception

        page = {}
        page['start_date'] = properties['Date']['date']['start']
        page['end_date'] =  properties['Date']['date']['end']
        page['name'] = properties['Name']['title'][0]['plain_text']
        page['icon'] = p['icon']

        calendar_objects.append(page)
    return  __list_to_map(calendar_objects)

def __list_to_map(pages) :
    map = {}
    for page in pages :
        l = []
        if (page['end_date']) : 
            diff = datetime.strptime(page['end_date'], '%Y-%m-%d') - datetime.strptime(page['start_date'], '%Y-%m-%d')
            #TODO datetime range for
            #print(diff)
            #print(type(diff)) #delta
        start_date = page['start_date']
        map[start_date] = [page] if map.get(start_date) is None else list(map.get(start_date))+[page]
    return map
if __name__ == '__main__':
    query_a_databases()