#!/usr/bin/env python
from base import *

#print(reddit.read_only)
#print(subreddit.title)

for submission in subreddit.stream.submissions():
  print(submission.title)
