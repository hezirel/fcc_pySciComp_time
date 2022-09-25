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
        self.hour = 0 if int(self.time.split(':')[0]) == 12 else int(self.time.split(':')[0])
        self.minute = int(self.time.split(':')[1])
        self.period = self.time.split(':')[2]
        self.starting_day = 0
        if self.period == 'PM':
            self.hour += 12

    def add_hours(self, hr):
        self.hour += hr
        while self.hour >= 24:
            self.starting_day += 1
            self.hour -= 24

    def add_minutes(self, mn):
        self.minute += mn
        if self.minute > 59:
            self.minute -= 60
            self.hour += 1

    def add_duration(self, duration):
        self.add_minutes(int(duration.split(':')[1]))
        self.add_hours(int(duration.split(':')[0]))
    
    def hour_str(self):
        if self.hour == 0:
            return '12'
        elif self.hour > 12:
            return str(f'{self.hour - 12:01}')
        else:
            return str(f'{self.hour:01}')

    def __repr__(self):
        return f'Final time is {self.hour_str()}:{self.minute} {self.period} {self.starting_day} days later'

def add_time(start, duration, day=None):

    begin = TimeObject(start)
    print(begin)
    begin.add_duration(duration)

    print(begin)
    return ("4:32")

add_time("11:43 PM", "24:20", "tueSday")
# Should be: 12:03 AM, Thursday (2 days later)
