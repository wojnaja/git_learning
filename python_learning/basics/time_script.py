#! /usr/bin/python3



from datetime import datetime

now = datetime.now()
current_time = now.strftime("%H:%M:%S")
print("Current time is :", current_time)

import pytz

tz_Prague = pytz.timezone('Europe/Prague')
datetime_PG = datetime.now(tz_Prague)
print("Prague time: ", datetime_PG.strftime("%Y %B %d %H:%M:%S"))

tz_Singapore = pytz.timezone('Asia/Singapore')
datetime_SGP = datetime.now(tz_Singapore)
print("Singapore time: ", datetime_SGP.strftime("%Y %B %d %H:%M:%S")) #%D will give date as well 



