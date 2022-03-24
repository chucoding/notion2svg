def write_calendar(request):
    svg = '''
        <?xml version="1.0" encoding="utf-8"?>
<!-- Generator: Adobe Illustrator 16.0.0, SVG Export Plug-In . SVG Version: 6.00 Build 0)  -->
<!DOCTYPE svg PUBLIC "-//W3C//DTD SVG 1.1//EN" "http://www.w3.org/Graphics/SVG/1.1/DTD/svg11.dtd">
<svg version="1.1" id="레이어_1" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" x="0px"
	 y="0px" width="600px" height="600px" viewBox="0 0 600 600" enable-background="new 0 0 600 600" xml:space="preserve">
<line fill="none" stroke="#000000" stroke-miterlimit="10" x1="138.027" y1="114.757" x2="138.027" y2="346.514"/>
<line fill="none" stroke="#000000" stroke-miterlimit="10" x1="138.027" y1="114.757" x2="373.162" y2="114.757"/>
<line fill="none" stroke="#000000" stroke-miterlimit="10" x1="373.162" y1="114.757" x2="373.162" y2="346.514"/>
<line fill="none" stroke="#000000" stroke-miterlimit="10" x1="138.027" y1="346.514" x2="373.162" y2="346.514"/>
</svg>
        '''

def write():
    # flask HttpResponse 
    # Content-Type => svg