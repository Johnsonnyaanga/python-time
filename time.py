from datetime import datetime,timedelta
now=datetime.now()
then=datetime(2015,8,20)
delta=now-then
print(delta.days)
print(delta.seconds)

 def get_n_days_before_date(self, date_format="%d %B %Y", days_before=120):
        date_n_days_ago = datetime.datetime.now() - timedelta(days=days_before)
        return date_n_days_ago.strftime(date_format) 
        

today=datetime.date.today
noon=datetime.time(12,0,0)
now=datetime.date.now()
#converting time zones
from datetime import datetime
from dateutil import tz
utc = tz.tzutc() 
local = tz.tzlocal()
utc_now=datetime.utcnow()
utc_now=utc_now.replace(tzinfo=utc)
local_now=utc_now.astimezone(local)

#time arithmetics
import datetime
today = datetime.date.today() 
print('Today:', today)
yesterday = today - datetime.timedelta(days=1) 
print('Yesterday:', yesterday)
tomorrow = today + datetime.timedelta(days=1) 
print('Tomorrow:', tomorrow)
print('Time between tomorrow and yesterday:', tomorrow - yesterday)
