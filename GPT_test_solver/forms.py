from django import forms
from .models import UserTests


class TestSolvForm(forms.ModelForm):
    test_name = forms.CharField(max_length=50, label="Test Name")

    class Meta:
        model = UserTests
        fields = ["test_name", "image"]


