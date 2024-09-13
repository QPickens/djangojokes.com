from django import forms

class JobApplicationForm(forms.Form):
    EMPLOYMENT_TYPE = (
        (None, '--Please choose--'),
        ('ft', 'Full-time'),
        ('pt', 'Part-time'),
        ('contract', 'Contract work')
    )

    DAYS = (
        (1, 'MON'),
        (2, 'TUE'),
        (3, 'WED'),
        (4, 'THU'),
        (5, 'FRI'),
        (6, 'SAT'),
        (7, 'SUN')
    )
    
    first_name = forms.CharField()
    last_name = forms.CharField()
    email = forms.EmailField()
    website = forms.CharField()
    employment_type = forms.CharField()
    start_date = forms.DateField(
        help_text='The earliest date you can start working.'
    )
    available_days = forms.MultipleChoiceField(
        choices=DAYS,
        help_text='Select all days that you can work.'
    )
    desired_hourly_wage = forms.DecimalField()
    cover_letter = forms.CharField()
    confirmation = forms.BooleanField(
        label='I certify that the information I have provided is true.'
    )