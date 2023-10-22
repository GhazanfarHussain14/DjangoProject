from django.forms import ModelForm
from .models import PersonalInformation
class PersonalDataForm(ModelForm):
    class Meta:
        model = PersonalInformation
        fields = '__all__'