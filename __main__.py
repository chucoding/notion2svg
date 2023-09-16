import base64

from modules import calendar

cal = calendar.NotionCalendar()

def main(args):

    body = cal.get_calendar(args.get("db"), args.get("auth"))
    encodedBody = base64.b64encode(body.encode('utf-8'))

    return {
        "statusCode": 200,
        "headers": { "Content-Type": "image/svg+xml" , "Cache-Control": "max-age=0"},
        "body": encodedBody.decode('utf-8'),
    }