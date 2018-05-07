from datetime import datetime
from django.db import models


class Theme(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Video(models.Model):
    title = models.CharField(max_length=100)
    date_uploaded = models.DateField()
    views = models.PositiveIntegerField()
    themes = models.ManyToManyField(Theme)

    def __str__(self):
        return '{}-{}'.format(self.title, self.views)

    def get_days_since_upload(self):
        today = datetime.today()
        diff = today.date() - self.date_uploaded
        return diff.days


class Comment(models.Model):
    is_positive = models.BooleanField()
    time = models.DateTimeField()
    video = models.ForeignKey(Video, related_name='comment',
                              on_delete=models.CASCADE)

    def __str__(self):
        return '{}-{}'.format(self.video.title, self.is_positive)


class Thumb(models.Model):
    is_positive = models.BooleanField()
    time = models.DateTimeField()
    video = models.ForeignKey(Video, related_name='thumb',
                              on_delete=models.CASCADE)

    def __str__(self):
        return '{}-{}'.format(self.video.title, self.is_positive)
