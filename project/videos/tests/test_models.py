from unittest.mock import patch

from datetime import datetime

from django.test import TestCase

from videos.models import (Video)


class VideoTest(TestCase):
    @patch('videos.models.datetime')
    def test_get_days_since_upload(self, _datetime):
        u"""this test will be verify if the video
        has a method to return days_since_upload"""

        _datetime.today.return_value = datetime(2018, 5, 4)

        video = Video()
        video.title = 'Video test from youtube'
        video.date_uploaded = datetime(2018, 1, 4).date()
        video.views = 1024
        video.save()

        self.assertEqual(video.get_days_since_upload(), 120)
