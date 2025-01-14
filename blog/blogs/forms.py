from django import forms
from .models import BlogPost, Comment

class BlogPostForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = ['title', 'text']  # Ensure these match the fields in the model



class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text']  # Assuming 'text' is the comment field
    
    text = forms.CharField(
        widget=forms.Textarea(attrs={'placeholder': 'Add a comment', 'class': 'form-control', 'rows': 4}),
        label=''  # Remove the label by setting it to an empty string
    )