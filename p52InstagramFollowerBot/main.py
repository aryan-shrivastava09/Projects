import time
from Insta_follower import InstaFollower

ib = InstaFollower()
ib.login()
time.sleep(5)
ib.find_followers()
