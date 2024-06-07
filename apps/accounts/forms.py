from allauth.account.forms import SignupForm, LoginForm
from crispy_forms.helper import FormHelper

class UserSignupForm(SignupForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.fields["email"].label = "Email"
        self.fields['password1'].help_text = None

class UserLoginForm(LoginForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.fields["password"].help_text = None