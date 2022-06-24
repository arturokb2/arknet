from django import forms
# from django.contrib.auth import authenticate



# PROGRAMMS = (
#             ('ambulatory/','Амбулаторные'),
#             ('reestr/','Реестры'),
#             ('convector/','Конвектор'),
#             ('hospital/','Стационар')
#             )
PROGRAMMS = (
            ('hospital/','Стационар'),
            )
class Form_auth(forms.Form):
# Класс Form_auth создает форму авторизации и выбора программы 
    username = forms.CharField(max_length=100,
                               widget=forms.TextInput(attrs={'class':'form-control',
                                                            'placeholder':'Введите логин'}))
    password = forms.CharField(max_length=100,
                               widget=forms.PasswordInput(attrs={'class':'form-control',
                                                                'placeholder':'Введите пароль'}))
    programms = forms.ChoiceField(choices=PROGRAMMS,widget=forms.Select(attrs={'class':'custom-select mr-sm-2',
                                                                                       'id':'inlineFormCustomSelect',
                                                                                       'name':'drop'}))