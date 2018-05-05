from datetime import datetime

from django.test import TestCase

from model_mommy.mommy import make

from videos.forms import VideoForm


class VideoFormTest(TestCase):
    def test_adding_video_wrong(self):
        theme_one = make('videos.Theme')
        theme_two = make('videos.Theme')
        theme_three = make('videos.Theme')

        data = {
            'title': 'video test',
            'date_uploaded': datetime(2016, 3, 22),
            'views': 1024,
            'themes': [theme_one.pk, theme_two.pk, theme_three.pk]
        }

        form = VideoForm(data=data)

        self.assertFalse(form.is_valid())

    def test_validation_video(self):
        u"""Test to verify the addion of the a video
        positive"""

        theme_one = make('videos.Theme')
        theme_two = make('videos.Theme')
        theme_three = make('videos.Theme')

        data = {
            'title': 'video test',
            'date_uploaded': datetime(2018, 3, 22),
            'views': 1024,
            'themes': [theme_one.pk, theme_two.pk, theme_three.pk]
        }

        form = VideoForm(data=data)

        self.assertTrue(form.is_valid())
