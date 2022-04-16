import os
from fastapi import Response

from logMng import logMng

logger = logMng().get_logger('app')

def write_calendar():
    print('write calendar')
    return '''
        <svg version="1.1" baseProfile="full" width="360" height="460" xmlns="http://www.w3.org/2000/svg">
            <rect width="100%" height="100%" fill="#3a3a3a" />
            <text x="10" y="60" font-size="45" fill="white">TIME 00:00</text>
            <text x="10" y="90" font-size="15" fill="skyblue">YYYY/MM/DD</text>
            <rect x="0" y="110" width="100%" height="2" fill="white" fill-opacity="0.5" stroke-opacity="0.8"/>
        </svg>
        '''

def write():
    # flask HttpResponse 
    # Content-Type => svg
    
    # postman > preview
    print('write in')
    return Response(content=write_calendar(), media_type="svg+xml")