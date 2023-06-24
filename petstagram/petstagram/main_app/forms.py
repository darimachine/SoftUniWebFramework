import datetime

from django import forms
from django.core.exceptions import ValidationError

from .helpers import DisabledFieldsFormMixin
from .models import Profile, PetPhoto, Pet


class BootstrapFormMixin:
    fields={}
    def _init_bootstrap_form_controls(self):
        for _ , field in self.fields.items():
            if not hasattr(field.widget, 'attrs'):
                setattr(field.widget,'attrs',{})
            if 'class' not in field.widget.attrs:
                field.widget.attrs['class']=''
            if field.widget.attrs['class'] !='form-control-file':
                field.widget.attrs['class']+=' form-control'
class CreateProfileForm(BootstrapFormMixin, forms.ModelForm):
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self._init_bootstrap_form_controls()
    class Meta:
        model=Profile
        fields = ('first_name','last_name','picture')
        widgets={
            'first_name': forms.TextInput(
                attrs={
                    'placeholder':'Enter first name'
                }),
            'last_name': forms.TextInput(
                attrs={
                    'placeholder': 'Enter last name'
                }),
            'picture': forms.TextInput(
                attrs={
                    'placeholder': 'Enter URL'
                }),
        }

class EditProfileForm(BootstrapFormMixin,forms.ModelForm):
    MIN_DATE_OF_BIRTH = datetime.date(1920, 1, 1)
    MAX_DATE_OF_BIRTH = datetime.date.today()
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._init_bootstrap_form_controls()
        self.initial['gender'] = Profile.DO_NOT_SHOW

    def clean_date_of_birth(self):
        date_of_birth = self.cleaned_data['date_of_birth']
        if date_of_birth<self.MIN_DATE_OF_BIRTH or self.MAX_DATE_OF_BIRTH<date_of_birth:
            raise ValidationError(
                f"Date of birth must be between {self.MIN_DATE_OF_BIRTH} and {self.MAX_DATE_OF_BIRTH}"
            )
        return date_of_birth
    class Meta:
        model = Profile
        fields = '__all__'
        widgets = {
            'first_name': forms.TextInput(
                attrs={
                    'placeholder': 'Enter first name'
                }),
            'last_name': forms.TextInput(
                attrs={
                    'placeholder': 'Enter last name'
                }),
            'picture': forms.TextInput(
                attrs={
                    'placeholder': 'Enter URL'
                }),
            'email':forms.EmailInput(
                attrs={
                    'placeholder':'Enter email'
                }),
            'description':forms.Textarea(
                attrs={
                    'placeholder':'Enter description',
                    'rows':3,
                }),
            'date_of_birth':forms.DateInput(
                attrs={
                    'type':'date',
                    'min':'1920-01-01',
                    'max':datetime.date.today()

                }
            )


        }
class DeleteProfileForm(forms.ModelForm):

    def save(self, commit=True):
        pets = self.instance.pet_set.all() # self.instance e PROFILA
        PetPhoto.objects.filter(tagged_pets__in=pets).delete()
        self.instance.delete()

        return self.instance
    class Meta:
        model = Profile
        fields = ()

class CreatePetForm(BootstrapFormMixin,forms.ModelForm):
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self._init_bootstrap_form_controls()


    class Meta:
        model = Pet
        fields = ('name','type','date_of_birth')
        widgets={
            'name':forms.TextInput(
                attrs={
                    'placeholder':'Enter pet name'
                }),
            'date_of_birth': forms.DateInput(
                attrs={
                    'type': 'date',
                    'min': '1920-01-01',
                    'max': datetime.date.today()

                }
            )

        }

class EditPetForm(BootstrapFormMixin,forms.ModelForm):
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self._init_bootstrap_form_controls()


    class Meta:
        model = Pet
        fields = ('name','type','date_of_birth')
        widgets={
            'name':forms.TextInput(
                attrs={
                    'placeholder':'Enter pet name'
                }),
            'date_of_birth': forms.DateInput(
                attrs={
                    'type': 'date',
                    'min': '1920-01-01',
                    'max': datetime.date.today()

                }
            )

        }

class DeletePetForm(BootstrapFormMixin,DisabledFieldsFormMixin,forms.ModelForm):

    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self._init_disabled_fields()
        self._init_bootstrap_form_controls()
    class Meta:
        model = Pet
        fields = ('name', 'type', 'date_of_birth')

    def save(self, commit=True):
        self.instance.delete() #self.instance e PROFILA
        return self.instance

class CreatePetPhotoForm(BootstrapFormMixin,forms.ModelForm):
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self._init_bootstrap_form_controls()

    def clean_tagged_pets(self):
        tagged_pets = self.cleaned_data['tagged_pets']
        if not tagged_pets:
            raise ValidationError(f"There should be atleast one pet")
        return tagged_pets
    class Meta:
        model = PetPhoto
        fields = ('photo','description','tagged_pets')
        widgets={
            'photo':forms.ClearableFileInput(
                attrs={
                    'class': 'form-control-file',
                }
               ),
            'description': forms.Textarea(
                attrs={
                    'rows':3,
                    'placeholder':'Enter description'

                }),
            # 'tagged_pets': forms.ModelMultipleChoiceField(
            #     queryset=Pet.objects.all(),
            #     widget=forms.CheckboxSelectMultiple(),
            # )


        }

class EditPetPhotoForm(BootstrapFormMixin,forms.ModelForm):
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self._init_bootstrap_form_controls()

    class Meta:
        model=PetPhoto
        fields=('photo','description','tagged_pets')
        widgets = {
            'photo': forms.ClearableFileInput(
                attrs={
                    'class': 'form-control-file',
                    'disabled':'disabled'
                }
            ),
            'description': forms.Textarea(
                attrs={
                    'rows': 3,

                }),
        }


