from fastapi import Response
from template.calendar import WhiteCalendar

def write():
    cal1 = WhiteCalendar()
    return Response(content=cal1.get_calendar(), headers={"Cache-Control": "max-age=0", "Content-Security-Policy": "image-src: 'unsafe-eval'; style-src: 'self'"}, media_type="image/svg+xml")