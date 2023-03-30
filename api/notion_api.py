import config
import requests
from datetime import datetime

def query_a_databases() :
    url = f"https://api.notion.com/v1/databases/{config.db}/query"

    headers = {
        "Accept": "application/json",
        "Notion-Version": "2022-02-22",
        "Authorization": f"Bearer secret_{config.auth}"
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