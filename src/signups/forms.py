from django import forms


from .models import SignUp

class SignUpForm(forms.ModelForm):
    class Meta:
        model = SignUp
        
def span3(self):
        self.fields['first_name'].widget.attrs = {'class':'span3'}