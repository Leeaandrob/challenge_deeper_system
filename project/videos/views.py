from django.urls import reverse_lazy
from django.views.generic import ListView, RedirectView

from videos.models import Video
from videos.utils import VideoInsights, PopularThemes


class RedirectToPopularThemeListView(RedirectView):
    url = reverse_lazy('popular_themes')


class PopularThemesListView(ListView):
    model = Video
    template_name = 'videos/popular_themes.html'
    context_object_name = 'videos'

    def get_themes(self, videos):
        data = [dict(
            video=video.id,
            themes=video.themes.values('id', 'name'),
            score=VideoInsights(video).get_score(),
        ) for video in videos]

        manager = PopularThemes(data)
        return manager.get_popular_themes()

    def get_context_data(self, **kwargs):
        context = super(PopularThemesListView, self).get_context_data(**kwargs)
        context['themes'] = self.get_themes(context['videos'])
        return context
