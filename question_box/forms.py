from django import forms
from django.forms import TextInput, Textarea


from .models import Question, Answer

class QuestionForm(forms.ModelForm):

    class Meta:
        model = Question
        fields = ('title','body',)
        widgets = {
            'title': TextInput(attrs={'class': 'form-title'}),
            'body':Textarea(attrs={'class': "form-body"}),
            }



class AnswerForm(forms.ModelForm):
    body = forms.CharField(widget=forms.Textarea, label='',)

    class Meta:
        model = Answer
        fields = ('body',)
        widgets = {
            'body':Textarea(attrs={'class': "form-body"}),
            }
        