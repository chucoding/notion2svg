from fastapi import Response
from api.calendar import BlackCalendar

def write():
    cal1 = BlackCalendar()
    return Response(content=cal1.get_calendar(), media_type="image/svg+xml")