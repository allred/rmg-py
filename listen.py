#!/usr/bin/env python
from base import *

#print(reddit.read_only)
#print(subreddit.title)

def getexif(file_temp):
  i = Image.open(file_temp.name)
  # FIXME: imgur strips exif, get exif from the smallest reddit thumbnail
  exif = i._getexif()
  #pp.pprint(inspect.getmembers(exif))
  for tag, value in exif.items():
    decoded = TAGS.get(tag, tag)
    pp.pprint(decoded)
    pp.pprint(value)
  return exif 

def retrieve_imgur(url):
  file_temp = tempfile.NamedTemporaryFile(
    delete=False,
    mode='w+b',
    prefix='rmg-imgur-',
    suffix='.jpg',
  )
  print(file_temp.name)
  m = re.search('^.*\/(\S+?)(\.jpg)*$', url)
  #print({"m": m.group(1)})
  img = imgur.get_image(m.group(1))
  #pp.pprint(inspect.getmembers(img))
  url_img = img.link
  urllib.request.urlretrieve(url_img, file_temp.name)
  return file_temp

def retrieve_reddit(url):
  file_temp = tempfile.NamedTemporaryFile(
    delete=False,
    mode='w+b',
    prefix='rmg-reddit-',
    suffix='.jpg',
  )
  print(file_temp.name)
  urllib.request.urlretrieve(url, file_temp.name)
  return file_temp

def get_rekog(path_img):
  img_bytes = open(path_img, 'rb')
  out = rekog.detect_labels(
    Image={
      "Bytes": img_bytes.read(),
    }
  )
  return out

for submission in subreddit.stream.submissions():
  #pp.pprint(inspect.getmembers(submission))
  #pp.pprint(submission.thumbnail)
  if not submission.preview:
    continue 
  submission_processed = False
  for top_level_comment in submission.comments:
    #pp.pprint(inspect.getmembers(top_level_comment.author.name))
    if top_level_comment.author.name == 'ratmongo':
      print("{0} {1} previously replied to by {2}".format(submission.id, submission.title, top_level_comment.author.name))
      submission_processed = True
      break
  if submission_processed:
    continue 
  #pp.pprint(submission.preview['images'][0]['resolutions'][-1]['url'])
  #url = submission.preview['images'][0]['resolutions'][-1]['url']
  #url_preview_reddit = submission.preview['images'][0]['resolutions'][0]['url'] 
  url_preview_reddit = submission.preview['images'][0]['resolutions'][0]['url'] 
  #print({"prev": url_preview_reddit})
  file_reddit = retrieve_reddit(url_preview_reddit)
  url_imgur = submission.url
  #print({"url": url_imgur})
  file_imgur = retrieve_imgur(url_imgur)
  '''
  #info = getexif(file_reddit)
  print(submission.title)
  '''
  found_labels = False
  out_rekog = get_rekog(file_imgur.name) 
  labels = {}
  if len(out_rekog['Labels']) > 0:
    labels['rekog'] = out_rekog['Labels']
    found_labels = True
  if found_labels:
    pass
    submission.reply(str(labels))
  print({"labels": labels})
