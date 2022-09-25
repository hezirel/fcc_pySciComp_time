weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
class TimeObject:

    def __init__(self, time, start_weekday):
        self.time = time.replace(' ', ':')
        self.hour = 0 if int(self.time.split(':')[0]) == 12 else int(self.time.split(':')[0])
        self.minute = int(self.time.split(':')[1])
        self.period = self.time.split(':')[2]
        self.starting_day = 0
        self.start_weekday = -1 if start_weekday == 'none' else weekdays.index(start_weekday.lower().capitalize())
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
            return str(self.hour - 12)
        else:
            return str(self.hour)

    def mn_str(self):
        return str(self.minute)

    def __repr__(self):
        hour = self.hour_str()
        minute = self.mn_str().zfill(2)
        period = 'AM' if self.hour < 12 else 'PM'
        if self.starting_day:
            day = f'(next day)' if self.starting_day < 2 else f'({self.starting_day} days later)'
        else: day = False
        if self.start_weekday > -1:
            weekday = weekdays[(self.start_weekday + self.starting_day) % 7]
        else: weekday = False

        return f'{hour}:{minute} {period}' + (f', {weekday}' if weekday else '') + (f' {day}' if day else '')

def add_time(start, duration, day="none"):

    begin = TimeObject(start, day)
    begin.add_duration(duration)
    ret = str(begin)
    print(ret)

    return (ret)

add_time("3:30 PM", "2:12", "Monday")
# Should be: 12:03 AM, Thursday (2 days later)
