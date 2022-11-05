import redis
from datetime import datetime as dt
from datetime import timedelta as td
from dateutil import parser

format = '%b %d %Y %I:%M%p'  # The format
redis_host = "localhost"
redis_port = 6379
redis_password = ""

current_time = dt.utcnow()
one_hour_ago = current_time - td(hours=1)

r = redis.StrictRedis(host=redis_host, port=redis_port, password=redis_password, decode_responses=True)
# r.delete("rates:time_created")
time_created = r.get("rates:time_created")
print(time_created)