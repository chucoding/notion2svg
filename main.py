from fastapi import FastAPI
from fastapi.logger import logger

from api import export_svg

app = FastAPI()

@app.get('/')
def hello_world():
    logger.debug('hello_world')
    return 'Hello World!'
 
@app.get('/calendar')
def show_calendar():
    return export_svg.write()

if __name__ == '__main__':
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=5000, reload=True, debug=True)