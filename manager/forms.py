from django import forms
from .models import Film, TeamMember


class FilmForm(forms.ModelForm):
    class Meta:
        model = Film
        fields = ['title', 'release_year']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['title'].widget.attrs['class'] = 'form-control'
        self.fields['release_year'].widget.attrs['class'] = 'form-control'


class TeamMemberForm(forms.ModelForm):
    class Meta:
        model = TeamMember
        fields = ['person', 'roles']

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.fields['person'].widget.attrs['class'] = 'form-control'
            self.fields['roles'].widget.attrs['class'] = 'form-control'


class FilmUpdateForm(forms.ModelForm):
    class Meta:
        model = Film
        fields = ['title', 'release_year']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['title'].widget.attrs['class'] = 'form-control'
        self.fields['release_year'].widget.attrs['class'] = 'form-control'


class TeamMemberUpdateForm(forms.ModelForm):
    class Meta:
        model = TeamMember
        fields = ['person', 'roles']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['person'].widget.attrs['class'] = 'form-control'
        self.fields['roles'].widget.attrs['class'] = 'form-control'
