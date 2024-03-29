import datetime
import hashlib
import json

from django.db import models
from django.forms.models import model_to_dict


# Create your models here.
class Agency(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    url = models.URLField(blank=True, null=True)
    rss = models.URLField(blank=True, null=True)
    title_tag = models.CharField(max_length=100, blank=True, null=True)
    pub_date_tag = models.CharField(max_length=100, blank=True, null=True)
    link_tag = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        verbose_name_plural = 'Agencies'

    def __str__(self):
        return self.name


class News(models.Model):
    token = models.CharField(max_length=128, blank=True, null=True)
    title = models.CharField(max_length=250, blank=True, null=True)
    pub_date = models.DateTimeField(blank=True, null=True)
    link = models.URLField(blank=True, null=True)
    agency = models.ForeignKey(Agency, on_delete=models.CASCADE, blank=True, null=True)
    creation = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'News'
        ordering = ['creation']

    def __str__(self):
        return self.title

    def json_chain(self):
        data = {
            "title": self.title,
            "pub_data": self.pub_date.timestamp(),
            "link": self.link,
            "agency": self.agency.name
        }
        return hashlib.sha512(json.dumps(data).encode()).hexdigest()

    def uncle_chain_weaver(self):
        try:
            last_news = News.objects.latest('creation')
            return hashlib.sha512(f'{last_news.token}{self.json_chain()}'.encode()).hexdigest()
        except:
            return hashlib.sha512(self.json_chain().encode()).hexdigest()

    def save(self, *args, **kwargs):
        if not self.token:
            self.token = self.uncle_chain_weaver()
        super(News, self).save()


class Config(models.Model):
    start_time = models.TimeField(blank=True, null=True)
    frequency = models.DurationField(blank=True, null=True)

    def __str__(self):
        return 'crawling at {}'.format(self.start_time)
