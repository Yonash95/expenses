from django import forms
from .models import Expense


class ExpenseSearchForm(forms.ModelForm):
    start_date = forms.DateField()
    end_date = forms.DateField()

    class Meta:
        model = Expense
        fields = ('name', 'amount', 'start_date', 'end_date')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].required = False
        self.fields['amount'].required = False
        self.fields['start_date'].required = False
        self.fields['end_date'].required = False
