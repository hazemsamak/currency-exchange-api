import requests
import json
import os
import redis
from datetime import datetime as dt
from datetime import timedelta as td
from dateutil import parser

redis_host = "redis-server"
redis_port = 6379
redis_password = ""

class PrayerTimesClient():
    def get_prayer_timings(self):
        print('Get prayer times from API')
        url = "http://api.aladhan.com/v1/timingsByCity?city=Dubai&country=United%20Arab%20Emirates&method=99&methodSettings=18.5,null,18.5&tune=2,2,-4,2,3,4,4,-1,0"

        payload={}
        headers = {}

        response = requests.request("GET", url, headers=headers, data=payload)
        response = json.loads(response.text)
        data = response["data"]["timings"]

        return data
    
    def get_cached_prayer_timings(self):
        _prayers_date_created = "prayers:time_created"
        _prayers_timings = "prayers:timings"
        format = '%b %d %Y'  # The format
        current_date = dt.utcnow().date()
        one_day_ago = current_date - td(days=1)
        
        r = redis.StrictRedis(host=redis_host, port=redis_port, password=redis_password, decode_responses=True)
        
        date_created_str = r.get(_prayers_date_created)
        if not date_created_str:
            date_created_str = one_day_ago.strftime(format)
            r.set(_prayers_date_created,date_created_str)
            
        date_created = parser.parse(date_created_str).date()
        if  current_date > date_created:
            prayer_timings = self.get_prayer_timings()
            current_time_str = current_date.strftime(format)
            r.set(_prayers_date_created,current_time_str)
            r.set(_prayers_timings, json.dumps(prayer_timings))
        else:
            prayer_timings = json.loads(r.get(_prayers_timings))

        return prayer_timings