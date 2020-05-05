from django.forms import Form, ModelForm, Textarea, TimeInput
from django import forms
from .models import BlogPost, Comment



class ContactForm(Form):
    name = forms.CharField(max_length=100)
    message = forms.CharField(widget=forms.Textarea)

    def send_email(self):
        #send mail using self.cleaned_date dictionary
        pass
    
class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ('blog_post', 'username', 'comment_content')
        
        widgets = {
            'blog_post': forms.HiddenInput(),
            'username': forms.HiddenInput(),
                       
        }


