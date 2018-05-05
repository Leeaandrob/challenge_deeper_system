from django.test import TestCase

from model_mommy.mommy import make

from videos.models import (Video, Theme, Thumb)
from videos.utils import Score


class ScoreTest(TestCase):
    def test_get_thumbs_up(self):
        u"""This test will verify the
        return of the method get_thumbs_up"""

        theme_one = make(Theme)
        theme_two = make(Theme)
        theme_three = make(Theme)

        video = make(Video)
        video.themes.add(theme_one)
        video.themes.add(theme_two)
        video.themes.add(theme_three)

        make(Thumb, video=video, is_positive=True, _quantity=5)
        make(Thumb, video=video, is_positive=False, _quantity=2)

        self.manager = Score(video=video)

        response = self.manager.get_thumbs_up()

        self.assertEqual(response, 0.714)
