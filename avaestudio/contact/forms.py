from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(label='Nombre', required=True, widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Escribe tu nopmbre...',
            'min_length': 3,
            'max_length':200,
        }
    ))
    email = forms.EmailField(label='Email', required=True, widget=forms.EmailInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Escribe tu correo...',
            'min_length': 3,
            'max_length':200,
        }
    ))
    content = forms.CharField(label='Contenido', required=True, widget=forms.Textarea(
        attrs={
            'class': 'form-control',
            'rows':3,
            'placeholder': 'Escribe un mensaje...',
            'min_length': 3,
            'max_length':200,
        }
    ))