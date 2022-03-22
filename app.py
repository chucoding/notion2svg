# flask server test

from flask import Flask
app = Flask(__name__)

import logMng
 
logger = logMng.get_logger('app')

@app.route('/')
def hello_world():
    logger.debug('hello_world')
    return 'Hello World!'
 
if __name__ == '__main__':
    app.run()