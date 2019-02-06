import json
from datetime import datetime

from crawler.feed_rss import FeedRss

url = 'http://revistaautoesporte.globo.com/rss/ultimas/feed.xml'

feed = FeedRss(url=url)

dict_feed = feed.genrate_dict_feed_content()

json = json.dumps(dict_feed, ensure_ascii=False)

file_result = open('result-{}.json'.format(datetime.now()), 'w')
file_result.write(json)
file_result.close()
