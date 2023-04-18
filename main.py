from fastapi import FastAPI, Response

from template.calendar import NotionCalendar

app = FastAPI()
cal = NotionCalendar()

@app.get('/')
def show_calendar():
    return Response(content=cal.get_calendar(), headers={"Cache-Control": "max-age=0", "Content-Security-Policy": "object-src href: 'unsafe-eval'"}, media_type="image/svg+xml")

if __name__ == '__main__':
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True, debug=True)