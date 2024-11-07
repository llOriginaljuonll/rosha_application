from allauth.account.forms import SignupForm, LoginForm
from crispy_forms.helper import FormHelper
from django import forms
from .models import CustomUser

class UserSignupForm(SignupForm):

    USER_TYPE_CHOICES = [
        ('', '--------'),
        ('self', 'self'),
        ('teacher', 'teacher'),
        ('parent', 'parent'),
    ]

    user_type = forms.ChoiceField(
        choices=USER_TYPE_CHOICES,
        label="Select your user type", 
        initial=''
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.label_class = "font-normal bg-rose-300"
        self.helper.form_tag = False
        self.fields["email"].label = "Email"

    def save(self, request):
        user = super(UserSignupForm, self).save(request)
        user.user_type = self.cleaned_data['user_type']
        user.save()
        return user

class UserLoginForm(LoginForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.fields["password"].help_text = None

        # remove remember field from login page.
        self.fields["remember"].label = False
        self.fields["remember"].widget.attrs.update({
            "class": "hidden"
        })