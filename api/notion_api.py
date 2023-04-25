from datetime import date, datetime

import requests

import config


def query_a_database():

    today = date.today()
    url = f"https://api.notion.com/v1/databases/{config.db}/query"
    headers = {
        "Authorization": f"Bearer secret_{config.auth}",
        "Accept": "application/json",
        "Notion-Version": "2022-02-22",
    }

    params = {
        "filter": {
            "property": "Date",
            "date": {
                "after": f"{today.year}-{today.month:02}-01"
            }
        }
    }
    response = requests.post(url, headers=headers, json=params)

    if response.status_code == 200:
        data = response.json()
        pages = data['results']

        calendar_objects = []
        for p in pages:
            properties = p['properties']  # TODO treat parsing error Exception

            page = {}
            page['start_date'] = properties['Date']['date']['start']
            page['end_date'] = properties['Date']['date']['end']
            page['name'] = properties['Name']['title'][0]['plain_text']
            page['icon'] = p['icon']

            calendar_objects.append(page)
    else:
        print(f"Error {response.status_code}: {response.text}")
    return list_to_map(calendar_objects)


def list_to_map(pages):
    map = {}
    for page in pages:
        # if (page['end_date']):
        # diff = datetime.strptime(
        #   page['end_date'], '%Y-%m-%d') - datetime.strptime(page['start_date'], '%Y-%m-%d')
        # print(diff)
        start_date = page['start_date']
        map[start_date] = [page] if map.get(
            start_date) is None else list(map.get(start_date))+[page]
        print(map)
    return map


if __name__ == '__main__':
    query_a_database()
