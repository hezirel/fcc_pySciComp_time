weekdays = {
    1: 'monday',
    2: 'tuesday',
    3: 'wednesday',
    4: 'thursday',
    5: 'friday',
    6: 'saturday',
    7: 'sunday'
}

class TimeObject:

    def __init__(self, time):
        self.time = time.replace(' ', ':')
        self.hour = int(self.time.split(':')[0])
        self.minute = int(self.time.split(':')[1])
        self.period = self.time.split(':')[2]
        if self.period == 'PM':
            self.hour += 12

    def add_hours(self, hr):
        self.hour += hr
        if self.hour > 23:
            self.hour -= 24

    def add_minutes(self, mn):
        self.minute += mn
        if self.minute > 59:
            self.minute -= 60
            self.hour += 1

    def __repr__(self):
        return f'Final time is {self.hour}:{self.minute} {self.period}'

def add_time(start, duration, day=None):

    start_time = TimeObject(start)
    print(start_time)
    return ("5:42 PM")

add_time("11:43 PM", "24:20", "tueSday")
# Should be: 12:03 AM, Thursday (2 days later)
