from django import forms


class HelloForm(forms.Form):
    check = forms.BooleanField(label='Checkbox', required=False)

class HelloForm1(forms.Form):
    data=[
        ('one', 'item1'),
        ('two', 'item2'),
        ('three', 'item3'),
        ('four', 'item4'),
    ]
    choice = forms.ChoiceField(label='Choice', choices=data)
    
