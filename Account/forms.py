from django import forms
from django.contrib.auth import authenticate
from django.contrib.auth.forms import UserCreationForm

from Account.models import User


class StudentRegistrationForm(UserCreationForm):
    """
        Registration Form for students with gender, first_name, last_name, email, password and
        confirm_password as input fields. Placeholders are also added to ensure ease of understanding
        It has been ensured that the email belongs to a student only and is a part of college database.
        This verification is performed using email_data.json which has been used to symbolize dummy
        data fetched from University's API.

    """

    def __init__(self, *args, **kwargs):
        UserCreationForm.__init__(self, *args, **kwargs)
        self.fields['gender'].required = True
        self.fields['first_name'].label = "First Name :"
        self.fields['last_name'].label = "Last Name :"
        self.fields['password1'].label = "Password :"
        self.fields['password2'].label = "Confirm Password :"
        self.fields['email'].label = "Email :"
        self.fields['gender'].label = "Gender :"

        self.fields['first_name'].widget.attrs.update(
            {
                'placeholder': 'Enter First Name',
            }
        )
        self.fields['last_name'].widget.attrs.update(
            {
                'placeholder': 'Enter Last Name',
            }
        )
        self.fields['email'].widget.attrs.update(
            {
                'placeholder': 'Enter Email',
            }
        )
        self.fields['password1'].widget.attrs.update(
            {
                'placeholder': 'Enter Password',
            }
        )
        self.fields['password2'].widget.attrs.update(
            {
                'placeholder': 'Confirm Password',
            }
        )

    class Meta:

        model = User

        fields = ['first_name', 'last_name', 'email', 'password1', 'password2', 'gender']

    def clean_gender(self):
        gender = self.cleaned_data.get('gender')
        if not gender:
            raise forms.ValidationError("Gender is required")
        return gender

    def save(self, commit=True):
        user = UserCreationForm.save(self, commit=False)
        user.role = "student"
        if commit:
            user.save()
        return user


class TeacherRegistrationForm(UserCreationForm):
    """
        Registration Form for teachers with gender, first_name, last_name, email, password and
        confirm_password as input fields. Placeholders are also added to ensure ease of understanding
        It has been ensured that the email belongs to a student only and is a part of college database.
        This verification is performed using email_data.json which has been used to symbolize dummy
        data fetched from University's API.

    """

    def __init__(self, *args, **kwargs):
        UserCreationForm.__init__(self, *args, **kwargs)
        self.fields['first_name'].required = True
        self.fields['last_name'].required = True
        self.fields['first_name'].label = "First Name"
        self.fields['last_name'].label = "Last Name"
        self.fields['password1'].label = "Password"
        self.fields['password2'].label = "Confirm Password"

        self.fields['first_name'].widget.attrs.update(
            {
                'placeholder': 'Enter First Name',
            }
        )
        self.fields['last_name'].widget.attrs.update(
            {
                'placeholder': 'Enter Last Name',
            }
        )
        self.fields['email'].widget.attrs.update(
            {
                'placeholder': 'Enter Email',
            }
        )
        self.fields['password1'].widget.attrs.update(
            {
                'placeholder': 'Enter Password',
            }
        )
        self.fields['password2'].widget.attrs.update(
            {
                'placeholder': 'Confirm Password',
            }
        )

    class Meta:
        model = User

        fields = ['first_name', 'last_name', 'email', 'password1', 'password2', ]

    def save(self, commit=True):
        user = UserCreationForm.save(self, commit=False)
        user.role = "teacher"
        if commit:
            user.save()
        return user


class UserLoginForm(forms.Form):
    """
        Form for user to log in using their email and password

    """

    email = forms.EmailField(
        widget=forms.EmailInput(attrs={'placeholder': 'Email', })
    )
    password = forms.CharField(strip=False, widget=forms.PasswordInput(attrs={

        'placeholder': 'Password',
    }))

    def clean(self, *args, **kwargs):
        email = self.cleaned_data.get("email")
        password = self.cleaned_data.get("password")

        if email and password:
            self.user = authenticate(email=email, password=password)
            try:
                user = User.objects.get(email=email)
            except User.DoesNotExist:
                raise forms.ValidationError("User Does Not Exist.")

            if not user.check_password(password):
                raise forms.ValidationError("Password Does not Match.")

            if not user.is_active:
                raise forms.ValidationError("User is not Active.")

        return super(UserLoginForm, self).clean(*args, **kwargs)

    def get_user(self):
        return self.user


class StudentProfileEditForm(forms.ModelForm):
    """
        Form for students to edit their profile ( first_name and last_name )

    """
    def __init__(self, *args, **kwargs):
        super(StudentProfileEditForm, self).__init__(*args, **kwargs)
        self.fields['first_name'].widget.attrs.update(
            {
                'placeholder': 'Enter First Name',
            }
        )
        self.fields['last_name'].widget.attrs.update(
            {
                'placeholder': 'Enter Last Name',
            }
        )

    class Meta:
        model = User
        fields = ["first_name", "last_name", "gender"]
