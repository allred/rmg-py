#!/usr/bin/env python
from base import *

def randstring(size=6, chars=string.ascii_uppercase + string.digits):
  return ''.join(random.choice(chars) for _ in range(size))

title = 'testsubmission ' + randstring()

r_imgur = imgur.upload_from_path(
  path = '/Users/mallred/Downloads/ratthumb.jpg',
)
print(r_imgur)

r_reddit = subreddit.submit(
  title=title,
  #selftext='',
  url=r_imgur['link'],
)
print(r_reddit)

