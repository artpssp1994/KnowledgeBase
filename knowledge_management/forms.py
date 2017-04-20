from django import forms
from knowledge_management.models import Page, Category, Comment, LikeComment
from tagging.forms import TagField
from tagging_autocomplete.widgets import TagAutocomplete


class CategoryForm(forms.ModelForm):
    name = forms.CharField(max_length=128, help_text="Please enter the category name.")
    # views = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
    # likes = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
    # slug = forms.CharField(widget=forms.HiddenInput(), required=False)

    # An inline class to provide additional information on the form.
    class Meta:
        model = Category
        fields = ('name',)


class PageForm(forms.ModelForm):
    title = forms.CharField(max_length=128, help_text="Please enter the title of the page.")
    data = forms.Textarea()
    tags = TagField(widget=TagAutocomplete(), initial="")
    category = forms.Select()
    views = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
    #slug = forms.CharField(widget=forms.HiddenInput(), required=False)

    class Meta:
        # Provide an association between the ModelForm and a model
        model = Page
        # exclude = ('category',)

        fields = ('title', 'data', 'views', 'category', 'tags')

class CommentForm(forms.ModelForm):
    data = forms.Textarea()
    like = forms.IntegerField(widget=forms.HiddenInput(), initial=0)

    class Meta:
        # Provide an association between the ModelForm and a model
        model = Comment
        # exclude = ('page',)
        fields = ('data',)

class LikeCommentForm(forms.ModelForm):
    like = forms.IntegerField(widget=forms.HiddenInput(), initial=0)

    class Meta:
        model = Comment
        fields = ('like',)

class DocumentForm(forms.Form):
    docfile = forms.FileField(
        label='Select a file',
    )