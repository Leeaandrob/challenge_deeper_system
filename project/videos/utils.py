from videos.models import (
    Thumb, Comment)


class PopularThemes:
    def __init__(self, data):
        self.data = data

    def get_themes(self):
        themes = []
        for item in self.data:
            for theme in item.get('themes'):
                if theme not in themes:
                    themes.append(theme.get('name'))

        return set(themes)

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
