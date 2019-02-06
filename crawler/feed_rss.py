import feedparser
import logging
from bs4 import BeautifulSoup

logger = logging.getLogger(__name__)


class FeedRss(object):
    
    def __init__(self, url):
        """[summary]
        
        Parameters
        ----------
        url : [String]
            [Url to rss]
        
        """

        self.url = url

    def __get_content_feed(self):
        try:
            feed = feedparser.parse(self.url)
        except Exception:
            logger.exception('Error to get rss', exc_info=True)
            feed_content = {}

        feed_content = feed.get('entries')
        return feed_content

    def genrate_dict_feed_content(self):
        list_dict = []

        itens = self.__get_content_feed()

        for item in itens:

            description = self.get_itens_description(item.get('description'))
            item_dict = {
                'title': item.get('title'),
                'link': item.get('link'),
                'description': description,
            }

            list_dict.append(item_dict)
        return list_dict

    def get_itens_description(self, description):
        list_itens = []
        soup = BeautifulSoup(description, features="html.parser")
        for tag in soup.find_all():
            data_item = self.__extract_data_item(tag)
            if data_item:
                list_itens.append(data_item)
        return list_itens

    def __extract_data_item(self, item):
        if item.name == 'img':
            image_data = self._get_image_data(item)
            if image_data:
                dict_image = {
                    'type': 'image',
                    'content': image_data
                }
                return dict_image
        elif item.name == 'ul':
            link_data = self._get_link_data(item)
            if link_data:
                dict_link = {
                    'type': 'links',
                    'content': link_data
                }
                return dict_link
        elif item.name == 'p':
            text_data = self._get_text_data(item)
            if text_data:
                dict_text = {
                    'type': 'text',
                    'content': text_data
                }
                return dict_text

    def _get_image_data(self, item):
        assert item.name == 'img', 'Item is not tag *img*'
        if item.parent.name == 'div' and item.has_attr('src'):
            return item.get('src')

    def _get_link_data(self, item):
        assert item.name == 'ul', 'Item is not tag *ul*'
        links = []
        for anchor in item.find_all('a'):
            if anchor.get('href'):
                links.append(anchor.get('href'))
        return links

    def _get_text_data(self, item):
        assert item.name == 'p', 'Item is not tag *p*'
        if item.get_text(strip=True):
            return item.get_text(strip=True)
