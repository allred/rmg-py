#!/usr/bin/env python
import os
import praw

reddit = praw.Reddit(
  user_agent='ratmongo'
)
subreddit = reddit.subreddit('ratmongo')
