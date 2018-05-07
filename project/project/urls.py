from django.contrib import admin
from django.urls import path

from videos.views import (
    PopularThemesListView, RedirectToPopularThemeListView)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', RedirectToPopularThemeListView.as_view(), name='main'),
    path('get_popular_themes/',
         PopularThemesListView.as_view(), name='popular_themes'),
]
