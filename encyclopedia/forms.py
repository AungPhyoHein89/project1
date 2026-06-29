from django import forms

class NewEntryForm(forms.Form):
  title = forms.CharField(
    label="Title:",
    widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter title'})
  )
  content = forms.CharField(
    label="Markdown content:",
    widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 10})
  )