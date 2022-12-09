from django.forms import forms, CharField, FileField, TextInput, IntegerField, DateTimeField, ImageField
from django.forms import ModelForm
from django import forms
# class ProductForm(forms.Form):
#     title = CharField(max_length=1000)
#     category = IntegerField()
#     description = CharField(widget=TextInput())
#     quantity = IntegerField()
#     manufacturing_date = DateTimeField(required=False)
#     image = FileField(required=False)


from manufacturing.models import Product, Category


class ProductForm(ModelForm):
    image = forms.FileField(required=False)

    class Meta:
        model = Product
        fields = [
            'title',
            'category',
            'description',
            'quantity',
            'manufacturing_date',
            'image',
        ]
        labels = {
            'manufacturing_date': 'Дата изготовления:',
            "quantity": "Количество:",
            "category": "Категория",
            "description": "Описание",
            "image": "Изображение",
            'title': "Hаименований "

        }
        widgets = {
            "title": TextInput(attrs={'class': 'form-control'}),
            "description": TextInput(attrs={'class': 'form-control'}),
            "quantity": forms.NumberInput(attrs={'class': 'form-control'}),
            "manufacturing_date": forms.DateInput(
                attrs={
                    'class': 'form-control',
                    'type': 'date',
                }
            ),
            'category': forms.Select(attrs={'class': 'form-control'}),
            'image': forms.FileInput(attrs={'class': 'form-control'})

        }
        error_messages = {
            'required': "Error"
        }

