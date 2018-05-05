from videos.models import (
    Thumb, Comment)


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
