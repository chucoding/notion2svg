from fastapi import Response
from datetime import datetime
import notion_api

def get_calendar():

    calendar_objects = notion_api.query_a_databases()
    print(calendar_objects)

    now = datetime.now()
    time = now.strftime('%X')
    date = now.date().isoformat()
    weeks = ["일","월","화","수","목","금","토"]
    x_idx = 20
    str_weeks = ''
    for w in weeks:
        str_weeks += "<text x='%d' y='145' font-size='15' fill='white'>%s</text>\n" % (x_idx, w)
        x_idx+=60
    return '''
        <!DOCTYPE svg PUBLIC
        "-//W3C//DTD SVG 1.1//EN"
        "http://www.w3.org/Graphics/SVG/1.1/DTD/svg11.dtd">
        <svg version="1.1" width="360" height="460" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
            <rect width="100%" height="100%" fill="#3a3a3a" />
            <text x="10" y="60" font-size="45" fill="white">{time}</text>
            <text x="10" y="90" font-size="15" fill="skyblue">{date}</text>
            <rect x="0" y="110" width="100%" height="2" fill="white" fill-opacity="0.5" stroke-opacity="0.8"/>
            {str_weeks}
            <rect x="0" y="170" width="100%" height="1" fill="white" fill-opacity="0.5" stroke-opacity="0.8"/>
            <rect x="0" y="230" width="100%" height="1" fill="white" fill-opacity="0.5" stroke-opacity="0.8"/>
            <rect x="0" y="290" width="100%" height="1" fill="white" fill-opacity="0.5" stroke-opacity="0.8"/>
            <rect x="0" y="350" width="100%" height="1" fill="white" fill-opacity="0.5" stroke-opacity="0.8"/>
            <rect x="0" y="410" width="100%" height="1" fill="white" fill-opacity="0.5" stroke-opacity="0.8"/>
        </svg>
        '''.format(
            time=time,
            date=date,
            str_weeks=str_weeks
        )

def get_calendar_object() :
    #TODO How to mapping object to calendar? is possible use z-index in svg??
    return 'test'

def write():
    return Response(content=get_calendar(), media_type="image/svg+xml")

if __name__ == '__main__':
    write()