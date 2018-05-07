from datetime import datetime

from django.urls import reverse
from django.test import TestCase

from model_mommy.mommy import make


class PopularThemeRedirectViewTest(TestCase):
    def test_correct_response(self):
        response = self.client.get(reverse('main'))

        self.assertRedirects(response, reverse('popular_themes'))


class PoupularThemesListViewTest(TestCase):
    def setUp(self):
        self.url = reverse('popular_themes')

        make('videos.Video', _quantity=10,
             date_uploaded=datetime(2018, 1, 10).date())

        theme_one = make('videos.Theme', name='one')
        theme_two = make('videos.Theme', name='two')
        theme_three = make('videos.Theme', name='three')

        video_one = make(
            'videos.Video', date_uploaded=datetime(2018, 4, 10).date(),
            views=1024,
        )

        video_two = make(
            'videos.Video', date_uploaded=datetime(2018, 4, 12).date(),
            views=1024,
        )

        video_three = make(
            'videos.Video', date_uploaded=datetime(2018, 4, 13).date(),
            views=1024,
        )

        # comments
        make('videos.Comment', video=video_one, is_positive=True, _quantity=20)
        make('videos.Comment', video=video_one, is_positive=False, _quantity=7)
        # thumbs
        make('videos.Thumb', video=video_one, is_positive=True, _quantity=5)
        make('videos.Thumb', video=video_one, is_positive=False, _quantity=2)

        # comments
        make(
            'videos.Comment',
            video=video_three, is_positive=True, _quantity=20)
        make(
            'videos.Comment',
            video=video_three, is_positive=False, _quantity=7)
        # thumbs
        make('videos.Thumb', video=video_three, is_positive=True, _quantity=5)
        make('videos.Thumb', video=video_three, is_positive=False, _quantity=2)

        video_one.themes.add(theme_one)
        video_two.themes.add(theme_two)
        video_three.themes.add(theme_three)

        video_two.themes.add(theme_one)
        video_three.themes.add(theme_two)
        video_one.themes.add(theme_three)

        video_one.themes.add(theme_one)
        video_two.themes.add(theme_two)
        video_three.themes.add(theme_three)

    def test_get_popular_themes(self):
        response = self.client.get(self.url)

        self.assertEqual(len(response.context['themes']), 3)
        self.assertEqual(response.context['themes'][0].get('name'), 'three')

    def test_correct_response(self):
        response = self.client.get(self.url)

        self.assertTemplateUsed('videos/popular_themes.html')
        self.assertEqual(response.status_code, 200)
