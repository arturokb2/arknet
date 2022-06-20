from django import forms
from .models import Load_1c

class Load_1c_forms(forms.ModelForm):
    class Meta:
        model = Load_1c
        fields = ('oper','sluch','sluch_10','user')
        widgets = {
                    'oper':forms.FileInput(attrs={'class':'form-control-file',
                                                  'id':'file_oper'}),
                    'sluch':forms.FileInput(attrs={'class':'form-control-file',
                                                   'id':'file_sluch'}),
                    'sluch_10': forms.FileInput(attrs={'class': 'form-control-file',
                                            'id': 'file_sluch_10'}),
                    'user':forms.NumberInput(attrs={'class':'form-control',
                                                   'id':'user_id'
                                                   }),
                    'type':forms.CharField()                             
                  }


#