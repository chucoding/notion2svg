from datetime import date

import requests


def query_a_database(db, auth):

    url = f"https://api.notion.com/v1/databases/{db}/query"
    headers = {
        "Authorization": f"Bearer secret_{auth}",
        "Accept": "application/json",
        "Notion-Version": "2022-02-22",
    }

    today = date.today()
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

"""
Returns:
    map (key : date, value : notion object)
"""
def list_to_map(pages):
    map = {}
    for page in pages:
        start_date = page['start_date']
        map[start_date] = [page] if map.get(
            start_date) is None else list(map.get(start_date))+[page]
    return map


if __name__ == '__main__':
    query_a_database()
