from django import forms
from .models import Item

INPUT_CLASSES = 'w-full px-4 py-3 rounded-xl border border-gray-200 bg-white text-gray-900 text-sm focus:outline-none focus:ring-2 focus:ring-teal-400 focus:border-transparent transition'

class NewItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ('category', 'name', 'description', 'price', 'image')
        widgets = {
            'category': forms.Select(attrs={'class': INPUT_CLASSES}),
            'name': forms.TextInput(attrs={'class': INPUT_CLASSES, 'placeholder': 'e.g. Nike Air Force 1'}),
            'description': forms.Textarea(attrs={'class': INPUT_CLASSES, 'rows': 4, 'placeholder': 'Describe the item — condition, size, colour...'}),
            'price': forms.NumberInput(attrs={'class': INPUT_CLASSES, 'placeholder': '0.00'}),
            'image': forms.ClearableFileInput(attrs={'class': 'block w-full text-sm text-gray-500 file:mr-4 file:py-2 file:px-4 file:rounded-lg file:border-0 file:text-sm file:font-semibold file:bg-teal-50 file:text-teal-600 hover:file:bg-teal-100 transition'}),
        }


class EditItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ('name', 'description', 'price', 'image', 'is_sold')
        widgets = {
            'name': forms.TextInput(attrs={'class': INPUT_CLASSES}),
            'description': forms.Textarea(attrs={'class': INPUT_CLASSES, 'rows': 4}),
            'price': forms.NumberInput(attrs={'class': INPUT_CLASSES}),
            'image': forms.ClearableFileInput(attrs={'class': 'block w-full text-sm text-gray-500 file:mr-4 file:py-2 file:px-4 file:rounded-lg file:border-0 file:text-sm file:font-semibold file:bg-teal-50 file:text-teal-600 hover:file:bg-teal-100 transition'}),
        }
