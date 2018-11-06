from django import forms
from .models import Cost


class CostEntryForm(forms.ModelForm):

    cost_choice = (('Cost', 'Cost'), ('Deposit', 'Deposit'))
    cost_type = forms.ChoiceField(label='Transection Type', choices=cost_choice)

    class Meta:
        model = Cost
        fields = ('purpose', 'cost_type', 'amount')
