from .models import Contacts
from high.models import Comments
from django import forms


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contacts
        fields = ['name', 'email', 'contact', 'message']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control user-name', 'placeholder': '姓名'}),
            'email': forms.EmailInput(attrs={'class': 'form-control mail', 'placeholder': '邮箱'}),
            'contact': forms.TextInput(attrs={'class': 'form-control pno', 'placeholder': '联系方式'}),
            'message': forms.Textarea(attrs={'class': 'form-control', 'rows': 6, 'placeholder': '留言'}),
        }
        error_messages = {
            'name': {'max_length': '姓名过长！', 'required': '请填写姓名！'},
            'email': {'invalid': '邮箱不合法！', 'required': '请填写邮箱！'},
            'contact': {'max_length': '联系方式过长！'},
            'message': {'required': '请填写留言！'},
        }


class SearchForm(forms.Form):
    key_words = forms.CharField(required=False, widget=forms.TextInput(attrs={'placeholder': '请输入您要搜索的关键字...'}))


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comments
        fields = ['content']
        error_messages = {
            'content': {'required': '请填写评论！'},
        }