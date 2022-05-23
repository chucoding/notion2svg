from abc import ABCMeta, abstractmethod
from datetime import datetime
from api import notion_api
import calendar;

class Calendar(metaclass=ABCMeta):

    now = datetime.now()
    time = now.strftime('%X')
    date = now.date().isoformat()
    month = now.strftime("%b %Y")
    
    #weeks = ["일","월","화","수","목","금","토"]
    weeks = ["Mon","Tue","Wed","Thu","Fri","Sat","Sun"]

    @abstractmethod
    def get_calendar(self):
        pass

    @abstractmethod
    def get_board(self):
        pass

    @abstractmethod
    def get_object(self):
        pass

class WhiteCalendar(Calendar) :
    def get_calendar(self):
        calendar_objects = notion_api.query_a_databases()
        print(calendar_objects)

        weeks = ''
        for i, w in enumerate(Calendar.weeks) :
            weeks += "<text x='%d' y='70' font-size='10px'>%s</text>\n" % (120*(i)+55, w)

        days = ''
        for i, week in enumerate(calendar.Calendar().monthdatescalendar(2022, 5)) :
            for j, day in enumerate(week) :
                print(day)
                days += "<text x='%d' y='%d' font-size='12px'>%s</text>" % (120*(j)+100, (80*(i)+100), day.strftime('%d'))
        return '''
            <!DOCTYPE svg PUBLIC
            "-//W3C//DTD SVG 1.1//EN"
            "http://www.w3.org/Graphics/SVG/1.1/DTD/svg11.dtd">
            <svg version="1.1" width="840" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
                <text x="10" y="40" font-size="20" font-weight="bold">{month}</text>
                {weeks}
                <rect x="600" y="80" width="240" height="480" fill="#F7F6F3"/>
                <path style="stroke:#E9E9E7;" d="M0,80 L840,80"/>
                <path style="stroke:#E9E9E7;" d="M0,160 L840,160"/>
                <path style="stroke:#E9E9E7;" d="M0,240 L840,240"/>
                <path style="stroke:#E9E9E7;" d="M0,320 L840,320"/>
                <path style="stroke:#E9E9E7;" d="M0,400 L840,400"/>
                <path style="stroke:#E9E9E7;" d="M0,480 L840,480"/>
                <path style="stroke:#E9E9E7;" d="M0,560 L840,560"/>
                <path style="stroke:#E9E9E7;" d="M120,80 L120,560"/>
                <path style="stroke:#E9E9E7;" d="M240,80 L240,560"/>
                <path style="stroke:#E9E9E7;" d="M360,80 L360,560"/>
                <path style="stroke:#E9E9E7;" d="M480,80 L480,560"/>
                <path style="stroke:#E9E9E7;" d="M600,80 L600,560"/>
                <path style="stroke:#E9E9E7;" d="M720,80 L720,560"/>
                <path style="stroke:#E9E9E7;" d="M840,80 L840,560"/>
                {days}
            </svg>
            '''.format(
                month=Calendar.month,
                weeks=weeks,
                days=days
            )

    def get_board(self):
        pass

    def get_object(self):
        pass

class BlackCalendar(Calendar) :
    def get_calendar(self):
        calendar_objects = notion_api.query_a_databases()
        #print(calendar_objects)

        x_idx = 20
        str_weeks = ''
        for w in Calendar.weeks:
            str_weeks += "<text x='%d' y='145' font-size='15' fill='white'>%s</text>\n" % (x_idx, w)
            x_idx+=60
        return '''
            <!DOCTYPE svg PUBLIC
            "-//W3C//DTD SVG 1.1//EN"
            "http://www.w3.org/Graphics/SVG/1.1/DTD/svg11.dtd">
            <svg version="1.1" width="360" height="460" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
                <rect width="100%" height="100%" fill="#3a3a3a" />
                <text x="10" y="60" font-size="45" fill="white">{time}</text>
                <text x="10" y="90" font-size="15" fill="skyblue">{date}</text>
                <rect x="0" y="110" width="100%" height="2" fill="white" fill-opacity="0.5" stroke-opacity="0.8"/>
                {str_weeks}
                <rect x="0" y="170" width="100%" height="1" fill="white" fill-opacity="0.5" stroke-opacity="0.8"/>
                <rect x="0" y="230" width="100%" height="1" fill="white" fill-opacity="0.5" stroke-opacity="0.8"/>
                <rect x="0" y="290" width="100%" height="1" fill="white" fill-opacity="0.5" stroke-opacity="0.8"/>
                <rect x="0" y="350" width="100%" height="1" fill="white" fill-opacity="0.5" stroke-opacity="0.8"/>
                <rect x="0" y="410" width="100%" height="1" fill="white" fill-opacity="0.5" stroke-opacity="0.8"/>
            </svg>
            '''.format(
                time=Calendar.time,
                date=Calendar.date,
                str_weeks=str_weeks
            )

    def get_board(self):
        pass

    def get_object(self):
        pass