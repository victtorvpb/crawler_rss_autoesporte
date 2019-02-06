from django.urls import path

from .views import GetFeedRss

app_name = 'api'

urlpatterns = [path('get_feed', GetFeedRss.as_view(), name="feed_rss")]