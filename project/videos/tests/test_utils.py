from django.test import TestCase

from model_mommy.mommy import make

from videos.models import (
    Video, Theme, Thumb, Comment)
from videos.utils import Score


class ScoreTest(TestCase):
    def setUp(self):
        theme_one = make(Theme)
        theme_two = make(Theme)
        theme_three = make(Theme)

        self.video = make(Video)
        self.video.themes.add(theme_one)
        self.video.themes.add(theme_two)
        self.video.themes.add(theme_three)

        self.manager = Score(video=self.video)

    def test_get_thumbs_up_zero(self):
        u"""This test will verify the
        return of the method get_thumbs_up when videos has 0
        thumbs"""

        response = self.manager.get_thumbs_up()

        self.assertEqual(response, 0)

    def test_get_thumbs_up(self):
        u"""This test will verify the
        return of the method get_thumbs_up"""

        make(Thumb, video=self.video, is_positive=True, _quantity=5)
        make(Thumb, video=self.video, is_positive=False, _quantity=2)

        response = self.manager.get_thumbs_up()

        self.assertEqual(response, 0.714)

    def test_good_comments_negative(self):
        u"""Test to verify the return of the method get good_comments
        of videos when video has a number of negative comments higher"""

        make(Comment, video=self.video, is_positive=True, _quantity=2)
        make(Comment, video=self.video, is_positive=False, _quantity=40)

        response = self.manager.get_good_comments()

        self.assertEqual(response, 0.048)

    def test_good_comments(self):
        u"""Test to verify the return of the method get good_comments
        of videos"""

        make(Comment, video=self.video, is_positive=True, _quantity=20)
        make(Comment, video=self.video, is_positive=False, _quantity=7)

        response = self.manager.get_good_comments()

        self.assertEqual(response, 0.741)

    def test_good_comments_zero(self):
        u"""Test to verify the return of the method get good_comments
        of videos when video has 0 comments"""

        response = self.manager.get_good_comments()

        self.assertEqual(response, 0)

    def test_get_positivity_factor(self):
        u"""Test to verify the return of the method get_positivity_factor
        """

        # comments
        make(Comment, video=self.video, is_positive=True, _quantity=20)
        make(Comment, video=self.video, is_positive=False, _quantity=7)

        # thumbs
        make(Thumb, video=self.video, is_positive=True, _quantity=5)
        make(Thumb, video=self.video, is_positive=False, _quantity=2)

        response = self.manager.get_positivity_factor()

        self.assertEqual(response, 0.733)
