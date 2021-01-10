from django.contrib.sitemaps import Sitemap
from django.shortcuts import reverse
from blog.models import Blogpost

class StaticViewsSitemap(Sitemap):

    priority = 0.8
    changefreq = 'yearly'

    def items(self):
        return ['/contact', '/search']

    def location(self, item):
        return item


class BlogSitemap(Sitemap):

    changefreq = 'daily'
    priority = 0.8

    def items(self):
        return Blogpost.objects.filter(status=1)


    def lastmod(self, obj):
        return obj.created_on