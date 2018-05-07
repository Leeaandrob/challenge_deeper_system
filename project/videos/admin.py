from django.contrib import admin

from videos.models import (
    Theme, Video, Comment, Thumb)
from videos.forms import VideoForm


class VideoThumbsInlineAdmin(admin.TabularInline):
    model = Thumb


class VideoCommentsInlineAdmin(admin.TabularInline):
    model = Comment


class VideoAdmin(admin.ModelAdmin):
    form = VideoForm
    model = Video
    inlines = [VideoThumbsInlineAdmin, VideoCommentsInlineAdmin]


admin.site.register(Theme)
admin.site.register(Video, VideoAdmin)
admin.site.register(Comment)
admin.site.register(Thumb)
