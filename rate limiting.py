import time

from ratelimiter import RateLimiter as RL
def limited(until):
    duration = int(round(until - time.time()))
    print("your rate has been limited by {} seconds".format(duration))

rate_limiter = RL(max_calls=2, period=3, callback=limited)

for i in range(3):
    with rate_limiter:
        print('Iteration', i)

