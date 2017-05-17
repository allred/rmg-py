#!/usr/bin/env python
import boto3
from imgurpython import ImgurClient
import inspect
import os
from PIL import Image 
from PIL.ExifTags import TAGS
import pprint
import praw
import tempfile
import urllib.request

imgur = ImgurClient(
  os.environ['RMG_IMGUR_CLIENT_ID'],
  os.environ['RMG_IMGUR_CLIENT_SECRET'],
)

pp = pprint.PrettyPrinter(indent=2)

reddit = praw.Reddit(
  user_agent='ratmongo'
)
subreddit = reddit.subreddit('ratmongo')

rekog = boto3.client('rekognition')
