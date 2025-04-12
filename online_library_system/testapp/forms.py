from django import forms
from .models import Author, Book, BorrowRecord

# Author Form
class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = ['name', 'email', 'bio']

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if Author.objects.filter(email=email).exists():
            raise forms.ValidationError("This email is already in use.")
        return email


# Book Form
class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'genre', 'published_date', 'author']
        widgets = {
            'published_date': forms.DateInput(attrs={'type': 'date'}),
        }


# BorrowRecord Form
class BorrowRecordForm(forms.ModelForm):
    class Meta:
        model = BorrowRecord
        fields = ['user_name', 'book', 'borrow_date', 'return_date']
        widgets = {
            'borrow_date': forms.DateInput(attrs={'type': 'date'}),
            'return_date': forms.DateInput(attrs={'type': 'date'}),
        }
