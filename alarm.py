from time import *
import datetime as dt


def get_sec(time_seconds):
    h, m, s = time_seconds.split(':')
    return int(h) * 3600 + int(m) * 60 + int(s)


def countdown():
    def set_time():
        alarm = input("Do you want to set an alarm?").lower()
        if alarm == "yes":
            alarmHr = int(input("Enter Hours: "))
            alarmMin = int(input("Enter Minutes: "))
            alarmSec = 0
            alarmDigital = input("AM/PM?: ").lower()

            if alarmDigital == "pm":
                alarmHr += 12

            return (alarmHr, alarmMin, alarmSec, alarm)
        else:
            return(alarm)

    alarmdigits = set_time()

    if "yes" in alarmdigits:
        alarmHr = alarmdigits[0]
        alarmMin = alarmdigits[1]
        alarmSec = alarmdigits[2]
        alarm
        cdt_h = dt.datetime.now().hour
        cdt_m = dt.datetime.now().minute
        cdt_s = dt.datetime.now().second

        cdt1 = f"{alarmHr:02}:{alarmMin:02}:{alarmSec:02}"
        cdt2 = f"{cdt_h:02}:{cdt_m:02}:{cdt_s:02}"
        format = "%H:%M:%S"
        time = dt.datetime.strptime(cdt1, format) - dt.datetime.strptime(cdt2, format)
        return (time, "yes")
    else:
        return ("no")


