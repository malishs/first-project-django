from django import forms

class Nameage(forms.Form):
    name = forms.CharField(label="Имя клиента")
    age = forms.IntegerField(label="Возраст клиента")

class UserForm(forms.Form):
    name = forms.CharField(label="Имя клиента",
        widget=forms.TextInput(attrs={"class": "myfield"}))
    age = forms.IntegerField(label="Возраст клиента",
        widget=forms.NumberInput(attrs={"class": "myfield"})) 

class Forma(forms.Form):
    name = forms.CharField(label="Имя", help_text="Введите ФИО")
    age = forms.IntegerField(label="Возраст", help_text="Введите возраст")