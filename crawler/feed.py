import feedparser
import logging

logger = logging.getLogger(__name__)


class Feed(object):
    def __init__(self, url):
        self.url = url

    def __get_content_feed(self):
        try:
            feed = feedparser.parse(self.url)
        except Exception:
            logger.exception('Error to get rss', exc_info=True)

        feed_content = feed.get('entries')

        return feed_content

    def genrate_dict_feed_content(self):
        list_dict = []
        
        itens = self.__get_content_feed()

        for item in itens:

            description = self.get_itens_description(item.get('description'))
            item_dict = {'title': item.get('title'),
                        'link': item.get('link'),
                        'description':description}
            
            
            list_dict.append(item_dict)
        import ipdb; ipdb.set_trace()
        return list_dict

    def get_itens_description(self, description):
        return description
