#!/usr/bin/env python
import inspect
import os
import pprint
import praw
import tempfile
import urllib.request

pp = pprint.PrettyPrinter(indent=2)

reddit = praw.Reddit(
  user_agent='ratmongo'
)
subreddit = reddit.subreddit('ratmongo')
