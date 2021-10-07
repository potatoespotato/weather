from django.contrib import sitemaps
from django.urls import reverse


class StaticPageViewSitemap(sitemaps.Sitemap):
    changefreq = 'daily'
    priority = 0.5

    def location(self, obj):
        return reverse('main:home')
