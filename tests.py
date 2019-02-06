import mock

from django.test import TestCase
from crawler.tests.mock_test import mock_get_feed, feed_test
from crawler.feed_rss import FeedRss

class test_feed_rss(TestCase):

    def test_case(self):
        with mock.patch.object(FeedRss,'_FeedRss__get_content_feed',new=mock_get_feed):
            feed = FeedRss('http://revistaautoesporte.globo.com/rss/ultimas/feed.xml')
            fed_content = feed.genrate_dict_feed_content()
            self.assertEqual(fed_content, feed_test)