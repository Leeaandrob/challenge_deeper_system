from operator import itemgetter

from videos.models import (
    Thumb, Comment)


def chunks(l, n):
    """Yield successive n-sized chunks from l."""
    for i in range(0, len(l), n):
        yield list(l[i:i + n])


class PopularThemes:
    def __init__(self, data):
        self.data = data

    def get_themes(self):
        themes = []
        for item in self.data:
            for theme in item.get('themes'):
                if theme not in themes:
                    theme.update({'score': 0})
                    themes.append(theme)

        return list({v['name']: v for v in themes}.values())

    def get_themes_score(self):
        themes_score = []
        score = 0

        for item in self.data:
            for video_theme in item.get('themes'):
                score += item.get('score')
                themes_score.append(
                    dict(
                        name=video_theme.get('name'),
                        id=video_theme.get('id'),
                        score=score
                    ))
                score = 0
        return themes_score

    def get_popular_themes(self):
        data = self.get_themes()

        for theme in data:
            for item in self.get_themes_score():
                if theme.get('name') == item.get('name'):
                    theme['score'] += item.get('score')
        return sorted(data, key=itemgetter('score'), reverse=True)


class VideoInsights:
    def __init__(self, video):
        self.video = video

    def get_score(self):
        time_factor = self.get_time_factor()
        positivity_factor = self.get_positivity_factor()

        return round(self.video.views * time_factor * positivity_factor, 3)

    def get_time_factor(self):
        return round(
            max(0, 1 - (self.video.get_days_since_upload() / 365)), 3)

    def get_positivity_factor(self):
        good_comments = self.get_good_comments()
        thumbs_up = self.get_thumbs_up()

        return round(0.7 * good_comments + 0.3 * thumbs_up, 3)

    def get_good_comments(self):
        positive_comments = Comment.objects.filter(
            video=self.video, is_positive=True).count()
        negative_comments = Comment.objects.filter(
            video=self.video, is_positive=False).count()

        try:
            return round(
                positive_comments / (positive_comments + negative_comments), 3)
        except ZeroDivisionError:
            return 0

    def get_thumbs_up(self):
        thumbs_up = Thumb.objects.filter(
            video=self.video, is_positive=True).count()
        thumbs_down = Thumb.objects.filter(
            video=self.video, is_positive=False).count()

        try:
            return round(thumbs_up / (thumbs_up + thumbs_down), 3)
        except ZeroDivisionError:
            return 0
