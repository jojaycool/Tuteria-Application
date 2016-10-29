import datetime

from django import forms

from unobase.questionnaire import forms as competition_forms
from unobase.age_gate.forms import AgeGateForm as BaseAgeGateForm

from guinnessnigeria import widgets
from guinnessnigeria.constants import COUNTRIES


class ContactUsForm(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    contact_number = forms.CharField(required=False)
    subject = forms.CharField(required=False)
    message = forms.CharField(widget=forms.Textarea)


class CustomQuestionnaire(competition_forms.Questionnaire):
    date_of_birth = forms.DateField()
    contact_me = forms.BooleanField(required=False)

    def __init__(self, *args, **kwargs):
        super(CustomQuestionnaire, self).__init__(*args, **kwargs)

        if self.user_obj.is_authenticated():
            if self.user_obj.contact_me:
                self.fields['contact_me'].initial = True

        self.fields['contact_me'].help_text = 'Yes, I would like to hear from Guinness'
        self.fields['date_of_birth'].widget = widgets.DateSelectorWidget()

    def clean_date_of_birth(self):
        age = self.cleaned_data['date_of_birth']

        if (datetime.date.today() - age).days / 365.0 < 18:
            raise forms.ValidationError(
                ('You do not meet the minumum age'
                 ' requirements to enter this competition')
            )

        return age

    def save(self, *args, **kwargs):
        obj = super(CustomQuestionnaire, self).save(*args, **kwargs)

        if self.user_obj.is_authenticated():
            if self.cleaned_data['contact_me'] and not self.user_obj.contact_me:
                self.user_obj.contact_me = True
                self.user_obj.save()

        return obj


class AgeGateForm(BaseAgeGateForm):
    """Add more countries"""
    location = forms.ChoiceField(choices=[(c, c) for c in COUNTRIES], required=False)
