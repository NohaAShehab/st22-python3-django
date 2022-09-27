from django import forms
from django.core.exceptions import NON_FIELD_ERRORS

from designs.models import Design


class DesignForm(forms.Form):
    name = forms.CharField()
    image = forms.ImageField()
    description = forms.CharField()
    price = forms.IntegerField()


class DesignModelForm(forms.ModelForm):
    class Meta:
        model = Design
        fields = '__all__'

        error_messages = {
            NON_FIELD_ERRORS: {
                'unique_together': "%(model_name)s's %(field_labels)s are not unique.",
            }
        }
