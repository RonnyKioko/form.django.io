from django import forms
from djangoform.model import StudeMobilis


class EmpForm(forms.ModelForm):
    class Meta:
        model = StudeMobilis
        fields = "__all__"
