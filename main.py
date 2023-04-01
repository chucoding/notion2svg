from fastapi import FastAPI
from fastapi.logger import logger

from api import export_svg

app = FastAPI()
 
@app.get('/')
def show_calendar():
    return export_svg.write()

if __name__ == '__main__':
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True, debug=True)