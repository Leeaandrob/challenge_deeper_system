from videos.models import (
    Thumb, Comment)


class Score:
    def __init__(self, video):
        self.video = video

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
