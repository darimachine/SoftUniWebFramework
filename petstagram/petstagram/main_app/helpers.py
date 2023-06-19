from django import forms

from .models import Profile


def get_profile():
    profiles= Profile.objects.all()
    if profiles:
        return profiles[0]
    return None

class DisabledFieldsFormMixin:
    disabled_fields ='__all__'
    fields = {}
    def _init_disabled_fields(self):
        for name, field in self.fields.items():
            if self.disabled_fields !='__all__' and name not in self.disabled_fields:
                continue
            if not hasattr(field.widget,'attrs'):
                setattr(field.widget,'attrs',{})
            if 'readonly' not in field.widget.attrs:
                field.widget.attrs['readonly'] =''
                field.widget.attrs['readonly']+='readonly'



