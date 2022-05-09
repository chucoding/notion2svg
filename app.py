from fastapi import FastAPI
from fastapi.responses import HTMLResponse

from utils import logMng
from api import export_svg

app = FastAPI()

logger = logMng().get_logger('app')

@app.get('/')
def hello_world():
    logger.debug('hello_world')
    return 'Hello World!'
 
@app.get('/calendar')
def get_calendar():
    return export_svg.write()

@app.get('/test', response_class=HTMLResponse)
def print():
    return export_svg.print()

if __name__ == '__main__':
    hello_world()