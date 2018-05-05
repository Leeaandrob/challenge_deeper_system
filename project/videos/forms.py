from datetime import datetime

from django import forms

from videos.models import Video


class VideoForm(forms.ModelForm):
    class Meta:
        model = Video
        fields = ['title', 'date_uploaded', 'views', 'themes']

    def clean_date_uploaded(self):
        today = datetime.today()
        data = self.cleaned_data['date_uploaded']
        if (today.date() - data).days > 365:
            raise forms.ValidationError("The date_uploaded can't be rhan")
        return data
