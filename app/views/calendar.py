import calendar
from abc import ABCMeta, abstractmethod
from datetime import datetime

from app.services import notion_api


class Calendar(metaclass=ABCMeta):
    now = datetime.now()
    date = now.strftime("%Y %b %m %X").split(" ")

    year, str_month, month, time = date[0], date[1], int(date[2]), date[3]
    today = now.date().isoformat()

    weeks = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]

    @abstractmethod
    def get_calendar(self):
        pass


class NotionCalendar(Calendar):

    def get_calendar(self):
        notion_pages = notion_api.query_a_database()
        svg_weeks = ''
        for i, w in enumerate(Calendar.weeks):
            svg_weeks += "<text x='%d' y='70' font-size='10px' fill='#9A9B97'>%s</text>\n" % (
                120*(i)+55, w)

        svg_days = ''
        stack = []
        for i, week in enumerate(calendar.Calendar().monthdatescalendar(int(self.year), self.month)):
            use_stack = True
            for j, day in enumerate(week):
                date = day.isoformat()
                # current month => fill black color for day / other month => fill gray color for day
                color = "black" if day.strftime(
                    '%b') == Calendar.now.strftime('%b') else "#9A9B97"

                # today => display red circle mark
                if Calendar.today == date:
                    color = "white"
                    svg_days += "<circle cx='%d' cy='%d' r='10' fill='#EB5757'/>" % (
                        120*(j)+105, (80*(i)+95))
                svg_days += "<text x='%d' y='%d' font-size='12px' fill='%s'>%s</text>" % (
                    120*(j)+100, (80*(i)+100), color, day.strftime('%d'))

                if stack and use_stack:
                    alpha = 25*(len(stack)-1)
                    if datetime.strptime(stack[-1].get('end_date'), '%Y-%m-%d').date() <= week[-1]:
                        width = 120 * \
                            ((datetime.strptime(
                                stack[-1].get('end_date'), '%Y-%m-%d').date() - week[0]).days+1)
                        stack.pop()
                    else:
                        use_stack = False
                        width = 120*7
                    svg_days += "<rect x='%d' y='%d' width='%d' height='20' rx='3' ry='3' stroke='#9A9B97' stroke-width='0.3' fill='white' />" % (
                        120*(j)+3, (80*(i)+105+alpha), width)

                # display notion_pages into calendar
                if notion_pages.get(date) is not None:
                    for k, notion_page in enumerate(notion_pages.get(date)):
                        if k > 1:
                            break

                        end_date = notion_page.get("end_date")
                        width = 120
                        alpha = 25*len(stack)

                        # merge start_date to end_date
                        if end_date is not None:
                            if datetime.strptime(end_date, '%Y-%m-%d').date() > week[-1]:
                                width += 120 * \
                                    (week[-1] - datetime.strptime(date,
                                     '%Y-%m-%d').date()).days
                            else:
                                width += 120 * \
                                    (datetime.strptime(end_date, '%Y-%m-%d') -
                                     datetime.strptime(date, '%Y-%m-%d')).days
                            stack.append(notion_page)
                            use_stack = False
                        notion_page_name = (bytes(notion_page["name"], 'utf-8')[0:12*int(width/120)+12*int(width/120-1)]).decode(
                            'utf-8')+"..." if len(bytes(notion_page["name"], 'utf-8')) > 12*int(width/120)+12*int(width/120-1) else notion_page["name"]
                        svg_days += "<rect x='%d' y='%d' width='%d' height='20' rx='3' ry='3' stroke='#9A9B97' stroke-width='0.3' fill='white' />" % (
                            120*(j)+3, (80*(i)+110+alpha), width-6)

                        if notion_page['icon'] is not None:
                            if notion_page['icon']['type'] == "emoji":
                                svg_days += "<text x='%d' y='%d' font-size='12px'>%s</text>" % (
                                    120*(j)+5, (80*(i)+125+alpha), notion_page['icon']['emoji']+" "+notion_page_name)
                            elif notion_page['icon']['type'] == "file":
                                svg_days += "<image x='%d' y='%d' width='15' height='15' href='%s' />" % (120*(
                                    j)+6, (68*(i)+112+alpha), notion_page['icon']['file']['url'].replace("&", "&amp;"))
                                svg_days += "<text x='%d' y='%d' font-size='12px'>%s</text>" % (
                                    120*(j)+26, (80*(i)+125+alpha), notion_page_name)
                        else:
                            svg_days += "<text x='%d' y='%d' font-size='12px'>%s</text>" % (
                                120*(j)+5, (80*(i)+125+alpha), notion_page_name)
        return '''
            <!DOCTYPE svg PUBLIC
            "-//W3C//DTD SVG 1.1//EN"
            "http://www.w3.org/Graphics/SVG/1.1/DTD/svg11.dtd">
            <svg version="1.1" width="840" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
                <text x="10" y="40" font-size="20" font-weight="bold">{month}</text>
                {svg_weeks}
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
                {svg_days}
            </svg>
            '''.format(
            month=self.str_month+" "+self.year,
            svg_weeks=svg_weeks,
            svg_days=svg_days
        )


class BlackCalendar(Calendar):
    def get_calendar(self):
        x_idx = 20
        str_weeks = ''
        for w in Calendar.weeks:
            str_weeks += "<text x='%d' y='145' font-size='15' fill='white'>%s</text>\n" % (
                x_idx, w)
            x_idx += 60
        return '''
            <!DOCTYPE svg PUBLIC
            "-//W3C//DTD SVG 1.1//EN"
            "http://www.w3.org/Graphics/SVG/1.1/DTD/svg11.dtd">
            <svg version="1.1" width="360" height="460" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
                <rect width="100%" height="100%" fill="#3a3a3a" />
                <text x="10" y="60" font-size="45" fill="white">{time}</text>
                <text x="10" y="90" font-size="15" fill="skyblue">{today}</text>
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
            today=Calendar.today,
            str_weeks=str_weeks
        )
