def write_calendar(request):
    svg = '''
        <svg version="1.1"
     baseProfile="full"
     width="300" height="200"
     xmlns="http://www.w3.org/2000/svg">
  <rect width="100%" height="100%" fill="yellow" />
  <circle cx="150" cy="100" r="80" fill="green" />
  <text x="150" y="125" font-size="60" text-anchor="middle" fill="white">외계공룡</text>
</svg>
        '''

def write():
    # flask HttpResponse 
    # Content-Type => svg
    
    # postman > preview
    return ''