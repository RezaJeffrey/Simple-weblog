from django import forms
from django.contrib.auth.models import User

class UserloginForm(forms.Form):
    email = forms.CharField(max_length=25,
                                 widget=forms.TextInput(
                                        attrs={'class':'form-control',
                                                'placeholder':'Username'}))

    password = forms.CharField(max_length=25,
                                 widget=forms.PasswordInput(
                                        attrs={'class':'form-control',
                                                'placeholder':'Password'}))


class UsersignupForm(forms.Form):
    username = forms.CharField(max_length=25,
                                 widget=forms.TextInput(
                                        attrs={'class':'form-control',
                                                'placeholder':'Username'}))

    email = forms.EmailField(widget=forms.EmailInput(
                                        attrs={'class':'form-control',
                                                'placeholder':'Email'}))



    password1 = forms.CharField(label= 'Password',max_length=25,
                                 widget=forms.PasswordInput(
                                        attrs={'class':'form-control',
                                                'placeholder':'Password'}))


    password2 = forms.CharField(label = 'Password',max_length=25,
                                 widget=forms.PasswordInput(
                                        attrs={'class':'form-control',
                                                'placeholder':'confirm password'}))

    def clean_email(self):
            mail = self.cleaned_data['email']
            user = User.objects.filter(email = mail)
            if user.exists():
                raise forms.ValidationError('this E-mail already exists, please enter another Email')
            return mail

    def clean_username(self):
        user_name = self.cleaned_data['username']
        user = User.objects.filter(username = user_name)
        if len(user)!= 0:
            raise forms.ValidationError('This username already exists')
        return user_name


    def clean(self):  #Overriding clean method 
        cleaned_data = super().clean()
        p1 = cleaned_data.get('password1')
        p2 = cleaned_data.get('password2')
        if p1 != p2:
            raise forms.ValidationError("Passwords doesn't match")



#     def clean_password2(self):
#         p1 = self.cleaned_data['password1']
#         p2 = self.cleaned_data['password2']

#         if p1 != p2:
#             raise forms.ValidationError("Passwords doesn't match")
            
#         return p1

    
