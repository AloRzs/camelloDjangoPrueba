#Formulario crud Productos


from django.forms import(
    ModelForm
)
from .models import Combo

class FormularioCombo(ModelForm):
    class Meta:
        model = Combo
        fields=['descripcion','stock','precio','foto']