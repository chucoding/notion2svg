# change fastapi server

from fastapi import FastAPI
app = FastAPI()

from logMng import logMng
from api import export_svg
 
logger = logMng().get_logger('app')

@app.get('/')
def hello_world():
    logger.debug('hello_world')
    return 'Hello World!'
 
@app.get('/svg/test')
def test_svg():
    print('test svg in')
    return export_svg.write()
    
if __name__ == '__main__':
    app.run()