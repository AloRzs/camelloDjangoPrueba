#Formulario crud Productos


from django.forms import(
    ModelForm,
    CharField,
    PasswordInput,
    TextInput,
    EmailInput,
    BooleanField,
)
from .models import Combo
from django.contrib.auth.models import User
from django.contrib.auth.forms import (AuthenticationForm,BaseUserCreationForm)

class FormularioCombo(ModelForm):
    class Meta:
        model = Combo
        fields=['descripcion','stock','precio','foto']



class FormularioRegistro(BaseUserCreationForm):
    def __init__(self, *args,**kargs):
        super().__init__(*args,**kargs)
        self.fields['password1'].widget.attrs = { 'class': 'form-control'}
        self.fields['password2'].widget.attrs = { 'class': 'form-control'}
        
    class Meta:
        model = User
        fields = [
            'username',
            'first_name',
            'last_name', 
            'email',
            'password1',
            'password2'
        ]
        widgets = {
            'username' : TextInput( attrs = { 'class':'form-control' }),
            'first_name' : TextInput( attrs = { 'class':'form-control' }),
            'last_name' : TextInput( attrs = { 'class':'form-control' }),
            'email' : EmailInput( attrs = { 'class':'form-control' }),
            'password1' : PasswordInput( attrs = { 'class':'form-control' }),
            'password2' : PasswordInput( attrs = { 'class':'form-control' })
        }


class FormularioLogin(AuthenticationForm):
    def __init__(self,*args,**kargs):
        super().__init__(*args,**kargs)
        self.fields['username'].widget.attrs={'class':'form-control'}
        self.fields['password'].widget.attrs={'class':'form-control'}