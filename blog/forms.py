from django import forms
from .models import Comment


class TicketForm(forms.Form):
    SUBJECT_CHOICES = (
        ('پیشنهاد', 'پیشنهاد'),
        ('انتقاد', 'انتقاد'),
        ('گزارش', 'گزارش'),
    )
    message = forms.CharField(widget=forms.Textarea, required=True, label="پیام")
    name = forms.CharField(max_length=250, required=True, label="نام",
                           widget=forms.TextInput(
                               attrs={'placeholder': 'نام', 'style': 'height: 30px', 'class': 'name_form'}))
    email = forms.EmailField(label="ایمیل")
    phone = forms.CharField(max_length=11, required=True, label="تلفن")
    subject = forms.ChoiceField(choices=SUBJECT_CHOICES, label="موضوع")

    def clean_phone(self):
        phone = self.cleaned_data['phone']
        if phone:
            if not phone.isnumeric():
                raise forms.ValidationError("شماره تلفن عددی نیست!")
            else:
                return phone


class CommentForm(forms.ModelForm):
    def clean_name(self):
        name = self.cleaned_data['name']
        if name:
            if len(name) < 3:
                raise forms.ValidationError("نام کوتاه است!")
            else:
                return name

    class Meta:
        model = Comment
        fields = ['name', 'message']
        widgets = {
            'message': forms.TextInput(attrs={'placeholder': 'متن'})
        }


class SearchForm(forms.Form):
    query = forms.CharField( )
