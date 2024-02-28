from django import forms
from .models import Booking,rasperry
from django import forms
from .models import Booking
import datetime
from .models import ProcessedImage
from .models import  Subscription

class DateInput(forms.DateInput):
    input_type = 'date'

class TimeInput(forms.TimeInput):
    input_type = 'time'
from django import forms
from .models import Booking
import datetime

class DateInput(forms.DateInput):
    input_type = 'date'

class TimeInput(forms.TimeInput):
    input_type = 'time'

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['indate', 'outdate', 'intime', 'outtime']
        widgets = {
            'indate': DateInput(),
            'outdate': DateInput(),
            'intime': TimeInput(),
            'outtime': TimeInput(),
        }

        labels = {
            'indate': 'Start Date',
            'intime': 'Start Time',
            'outdate': 'Out Date',
            'outtime': 'Out Time',
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        current_date = datetime.date.today()
        current_time = datetime.datetime.now().time().strftime('%H:%M')
        self.fields['indate'].widget.attrs['min'] = str(current_date)
        self.fields['outdate'].widget.attrs['min'] = str(current_date)
        self.fields['intime'].widget.attrs['min'] = current_time
        self.fields['outtime'].widget.attrs['min'] = current_time

from django import forms
from django.core.validators import MaxLengthValidator

# class AddSlot(forms.ModelForm):
#     latitude = forms.CharField(label='Latitude', required=False, widget=forms.TextInput, validators=[MaxLengthValidator(limit_value=20)])
#     longitude = forms.CharField(label='Latitude', required=False, widget=forms.TextInput, validators=[MaxLengthValidator(limit_value=20)])

#     class Meta:
#         model = Park
#         fields = '__all__'
#         labels = {
#             'img': 'Slot Image',
#             'head': 'Slot Name',
#             'desc': 'Total Slots Available',
#             'price': 'Slot Price',
#         }
class rasperryForm(forms.ModelForm):
    class Meta:
        model = rasperry
        fields = ['entryvnumber', 'head', 'entrydate', 'entrytime', 'exitdate', 'exittime']


class ProcessedImageForm(forms.ModelForm):
    class Meta:
        model = ProcessedImage
        fields = ['image_data', 'processed_text']
        
# forms.py


class SubscriptionForm(forms.ModelForm):
    class Meta:
        model = Subscription
        fields = ['sub_type', 'price', 'validity', 'features']
        widgets = {
            'sub_type': forms.TextInput(attrs={
                "class": "form-control ",
                'id':'sub_type'
            }),
            'price': forms.TextInput(attrs={
                "class": "form-control ",
                'id':"price",   
               
            }),
           'validity': forms.Select(attrs={
                "class": "form-control ",
                'id':'validity'
            }),
            'features': forms.TextInput(attrs={
                "class": "form-control ",
                'id':"features",
                'placeholder': 'Enter the Features'
            }),
            
         }
from django import forms
from .models import UserFeedback

class FeedbackForm(forms.ModelForm):
    class Meta:
        model = UserFeedback
        fields = ['feedback_text']
        widgets = {
            'feedback_text': forms.Textarea(attrs={'placeholder': 'Feedback', 'class': 'form-control shadow-none', 'cols': 30, 'rows': 5}),
        }