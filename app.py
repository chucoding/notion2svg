# flask server test

from flask import Flask
app = Flask(__name__)

from logMng import logMng
from api import export_svg
 
logger = logMng().get_logger('app')

@app.route('/')
def hello_world():
    logger.debug('hello_world')
    return 'Hello World!'
 
@app.route('/svg/test')
def test_svg():
    return export_svg.write()
    
if __name__ == '__main__':
    app.run()