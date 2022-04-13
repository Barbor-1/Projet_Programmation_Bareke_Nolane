import datetime

class format_time(): # TEMPS GMT
    def __init__(self):
        self.string = ""
    def formatTime(self, string):
        # time example  2022-04-13T00:00:00+02:00

        self.string = string
        self.date = self.string.split('T')[0] # 2022-04-13
        day = int(self.date.split('-')[2])
        month = int(self.date.split('-')[1])
        year = int(self.date.split('-')[0])

        temp = self.string.split('T')[1]
        time = temp.split('+')[0] # 00:00:00

        hour = int(time.split(':')[0])
        minute = int(time.split(':')[1])
        seconds = int(time.split(':')[2])

        time_zone = temp.split('+')[1] #02:00
        hour += int(time_zone.split(':')[0])
        minute += int(time_zone.split(':')[1])

        self.datetime = datetime.datetime(hour=hour, minute=minute, second=seconds, day=day, month=month, year=year)

    def getDateTime(self):
        return self.datetime
    def __repr__(self):
        return str(self.datetime)


