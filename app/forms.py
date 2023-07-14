from django.forms import ModelForm
from app.models import Personagens


# Create the form class.
class PersonagensForm(ModelForm):
    class Meta:
        model = Personagens
        fields = ["personagem", "jogo", "ano"]
