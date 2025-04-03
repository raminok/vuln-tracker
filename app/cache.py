from cachetools import TTLCache

 # cache with 100 value and I hour lifttime
cache = TTLCache(maxsize=100, ttl=3600) 
