from django import forms

class Nameage(forms.Form):
    name = forms.CharField(label="Имя клиента")
    age = forms.IntegerField(label="Возраст клиента")

class FileSelected(forms.Form):
    file = forms.FileField(label="Файл")

    