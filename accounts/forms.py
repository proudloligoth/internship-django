from django import forms

from .models import User, Address


class ProfileDetailForm(forms.ModelForm):
    email = forms.EmailField()
    #first_name = forms.CharField(max_length=)
    address = forms.ModelMultipleChoiceField(queryset=Address.objects.all())
    # cart = forms.InlineForeignKeyField(widget=forms.HiddenInput())

    class Meta:
        model = User


class ProfileUpdateForm(forms.ModelForm):

    error_message = {'duplicate_email': 'A user with thatemail already exits',
        'password_mismatch': 'The two password fields didn\'t match',
        'incorect_password': 'Password is invalid'}
    first_name = forms.CharField(label='First name', max_length=20, widget=forms.TextInput)
    last_name = forms.CharField(label='Last name', max_length=20, widget=forms.TextInput)
    email = forms.EmailField(label='E-mail', max_length=30, widget=forms.EmailInput)
    phone = forms.CharField(label='Mobile', max_length=10, widget=forms.NumberInput)
    address = forms.ModelMultipleChoiceField(queryset=Address.objects.all())
    cur_pwd = forms.CharField(label='Current password', widget=forms.PasswordInput)
    new_pwd1 = forms.CharField(label='New password', widget=forms.PasswordInput)
    new_pwd2 = forms.CharField(label='New password confirmation', widget=forms.PasswordInput,
                                help_text="Enter the same password as above, for verification.")

    class Meta:
        model = User

    def clean_cur_pwd(self):
        cur_pwd = self.cleaned_data['cur_pwd']
        if cur_pwd and User.password != cur_pwd:
            raise forms.ValidationError(self.error_message['incorect_password'],
                code='incorrect_password')
        return cur_pwd

    def clean_password(self):
        pwd1 = self.cleaned_data.get('pwd1')
        pwd2 = self.cleaned_data.get('pwd2')
        if pwd1 and pwd2 and pwd1 != pwd2:
            raise forms.ValidationError(
                self.error_messages['password_mismatch'],
                code='password_mismatch',
            )
        return pwd2

class RegistrationForm(forms.ModelForm):
    """
    A form that creates a user, with no privileges, from the given username and
    password.
    """
    error_messages = {
        'duplicate_email': "A user with that email already exists.",
        'password_mismatch': "The two password fields didn't match.",
    }
    email = forms.RegexField(label="E-mail", max_length=30,
                             regex=r'^[\w.@+-]+$',
                             help_text="Required. 30 characters or fewer. Letters, digits and "
                                       "@/./+/-/_ only.",
                             error_messages={
                                 'invalid': "This value may contain only letters, numbers and "
                                            "@/./+/-/_ characters."})
    password1 = forms.CharField(label="Password",
                                widget=forms.PasswordInput)
    password2 = forms.CharField(label="Password confirmation",
                                widget=forms.PasswordInput,
                                help_text="Enter the same password as above, for verification.")

    # cart = forms.ModelChoiceField(queryset=Cart.objects.all())

    class Meta:
        model = User
        fields = ("email", "password1", "password2", "first_name", "last_name", "phone")

    def clean_email(self):
        # Since User.username is unique, this check is redundant,
        # but it sets a nicer error message than the ORM. See #13147.
        email = self.cleaned_data["email"]
        try:
            User._default_manager.get(email=email)
        except User.DoesNotExist:
            return email
        raise forms.ValidationError(
            self.error_messages['duplicate_email'],
            code='duplicate_email',
        )

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError(
                self.error_messages['password_mismatch'],
                code='password_mismatch',
            )
        return password2

    def save(self, commit=True):
        user = super(RegistrationForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        user.first_name = self.cleaned_data.get("first_name")
        user.last_name = self.cleaned_data.get("last_name")
        user.phone = self.cleaned_data.get("phone")
        if commit:
            user.save()
        return user

#cart
#order
#order history