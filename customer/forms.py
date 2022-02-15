from django import forms


# def not_email_form(value):
#     if value:
#         raise Error

def min_length_2_validator(value):
    if len(value) < 2:
        raise forms.ValidationError('name은 두글자 이상이여야 합니다.')

class CustomerForm(forms.Form):
    name = forms.CharField(validators=[min_length_2_validator])
    birthdate = forms.DateField()
    email = forms.EmailField()
    male_or_female = [('1', '남자'), ('2', '여자')]
    gender = forms.ChoiceField(widget=forms.RadioSelect, choices = male_or_female)
