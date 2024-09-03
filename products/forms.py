from django import forms

from products.services import get_all_model_objects, get_max_product_price
from .models import Brand, Category


class XlsxImportForm(forms.Form):
    xlsx_file = forms.FileField() 


class SearchAndFilterForm(forms.Form):    
    max_product_price = get_max_product_price()

    q = forms.CharField(
        max_length=100, 
        required=False, 
        label='Введите запрос', 
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Найти товар'
        })
    )

    categories = forms.MultipleChoiceField( 
        choices=((brand.id, brand.title) for brand in get_all_model_objects(Category)), 
        widget=forms.CheckboxSelectMultiple(), 
        required=False
    )

    price_min = forms.DecimalField(
        max_digits=10,
        decimal_places=2,
        required=False,
        label='Мин. цена',
        widget=forms.NumberInput(
            attrs={ 
                'class': 'form-control', 
                'placeholder': f'0 ₽', 
                'min': 0,
                'step': 100,
                'type': 'text',
            }
        ), 
    )
    
    price_max = forms.DecimalField(
        max_digits=10,
        decimal_places=2,
        required=False,
        widget=forms.NumberInput(
            attrs={ 
                'class': 'form-control', 
                'placeholder': f'{max_product_price} ₽', 
                'min': 0,
                'step': 100,
            }
        ), 
    )

    brands = forms.MultipleChoiceField( 
        choices=((brand.id, brand.title) for brand in get_all_model_objects(Brand)), 
        widget=forms.CheckboxSelectMultiple(), 
        required=False
    )

    is_in_stock = forms.BooleanField( 
        required=False,
        label_suffix='',
        label='В наличии',
        widget=forms.CheckboxInput()
    )
 
    def clean_price_max(self): 
        cd = self.cleaned_data
        price_min = cd.get('price_min')
        price_max = cd.get('price_max')
        if price_max and price_min: 
            if price_min > price_max: 
                raise forms.ValidationError('Максимальная цена не может быть меньше минимальной') 
        return price_max
