from django import forms
from app.models import Expense

class ExpenseF(forms.ModelForm):
    class Meta:
        model = Expense
        fields = ['Name', 'Date_of_Expence', 'Description', 'Amount', 'Category']
        widgets = {
            'Date_of_Expence': forms.DateInput(attrs={'type': 'date'}, format='%Y-%m-%d'),
        }
        input_formats = ['%Y-%m-%d']

    def save(self, commit=True, **kwargs):
        instance = super().save(commit=False)

        # Check if 'created_by' is present in the form's initial data
        if 'created_by' in self.initial:
            instance.created_by = self.initial['created_by']

        if commit:
            instance.save()

        return instance
