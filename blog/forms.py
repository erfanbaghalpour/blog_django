from django import forms


class TicketForm(forms.Form):
    SUBJECT_CHOICES = (
        ('پیشنهاد', 'پیشنهاد'),
        ('انتقاد', 'انتقاد'),
        ('گزارش', 'گزارش'),
    )
    message = forms.CharField(widget=forms.Textarea, required=True, label="پیام")
    name = forms.CharField(max_length=250, required=True, label="نام")
    email = forms.EmailField(label="ایمیل")
    phone = forms.CharField(max_length=11, required=True, label="تلفن")
    subject = forms.ChoiceField(choices=SUBJECT_CHOICES, label="موضوع")
