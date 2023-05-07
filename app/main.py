
import uvicorn
from dotenv import load_dotenv
from fastapi import FastAPI, Response

from app.views.calendar import NotionCalendar

load_dotenv()

app = FastAPI()
cal = NotionCalendar()


@app.get('/')
def show_calendar():
    return Response(content=cal.get_calendar(), headers={"Cache-Control": "max-age=0"}, media_type="image/svg+xml")


if __name__ == '__main__':
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True, debug=True)
