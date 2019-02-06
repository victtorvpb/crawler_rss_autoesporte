from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from crawler.feed_rss import FeedRss


class GetFeedRss(APIView):
    def get(self, request):
        feed = FeedRss(url='http://revistaautoesporte.globo.com/rss/ultimas/feed.xml')
        feed_dict = feed.genrate_dict_feed_content()
        return Response(feed_dict, status=status.HTTP_200_OK)