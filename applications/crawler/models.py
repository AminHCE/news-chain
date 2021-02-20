from django.db import models


# Create your models here.
class Agency(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    url = models.URLField(blank=True, null=True)
    rss = models.URLField(blank=True, null=True)
    title_tag = models.CharField(max_length=100, blank=True, null=True)
    pub_date_tag = models.CharField(max_length=100, blank=True, null=True)
    link_tag = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.name


class News(models.Model):
    title = models.CharField(max_length=250, blank=True, null=True)
    pub_date = models.DateTimeField(blank=True, null=True)
    link = models.URLField(blank=True, null=True)
    agency = models.ForeignKey(Agency, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.title
