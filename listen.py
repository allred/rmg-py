#!/usr/bin/env python
from base import *

#print(reddit.read_only)
#print(subreddit.title)

def get_exif(file_temp):
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
  log_ts("{} -> {}".format(url, file_temp.name))
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

def submission_has_preview(submission):
  print("'{} {}' waiting for preview: ".format(submission.id, submission.title, end=""))
  for n in range(4): 
    time.sleep(n)
    if not hasattr(submission, 'preview'):
      print("{} ".format(n), end="")
    else:
      print(" ")
      return True 
  else:
      print(" ")
      return False

def log_ts(s):
  ts = datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S')
  print("{} {}".format(ts, s))

for submission in subreddit.stream.submissions():
  #pp.pprint(inspect.getmembers(submission))
  #pp.pprint(submission.thumbnail)
  submission_processed = False
  for top_level_comment in submission.comments:
    if top_level_comment.author.name == 'ratmongo':
      log_ts("'{0} {1}' previously replied to by {2}".format(submission.id, submission.title, top_level_comment.author.name))
      submission_processed = True
      break
  if not submission_processed and not submission_has_preview(submission):
    log_ts("'{0} {1}' no preview".format(submission.id, submission.title))
    submission.reply("no image preview found")
    submission_processed = True
  if submission_processed:
    continue 
  #pp.pprint(submission.preview['images'][0]['resolutions'][-1]['url'])
  #url = submission.preview['images'][0]['resolutions'][-1]['url']
  #url_preview_reddit = submission.preview['images'][0]['resolutions'][0]['url'] 
  #file_reddit = retrieve_reddit(url_preview_reddit)
  url_imgur = submission.url
  file_imgur = retrieve_imgur(url_imgur)
  found_labels = False
  out_rekog = get_rekog(file_imgur.name) 
  labels = {}
  if len(out_rekog['Labels']) > 0:
    labels['rekog'] = out_rekog['Labels']
    found_labels = True
  submission.reply(str(labels))
  print({"labels": labels})
