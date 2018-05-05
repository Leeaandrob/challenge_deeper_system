from videos.models import Thumb


class Score:
    def __init__(self, video):
        self.video = video

    def get_thumbs_up(self):
        thumbs_up = Thumb.objects.filter(
            video=self.video, is_positive=True).count()
        thumbs_down = Thumb.objects.filter(
            video=self.video, is_positive=False).count()

        return round(thumbs_up / (thumbs_up + thumbs_down), 3)
