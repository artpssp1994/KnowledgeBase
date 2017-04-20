from django.db import models
from datetime import datetime
from django.contrib.auth.models import User
from tagging_autocomplete.models import TagAutocompleteField
# Create your models here.

my_default_errors = {
    'required': 'This field is required',
    'invalid': 'Enter a valid value'
}

class Super_category(models.Model):
    name = models.CharField(max_length=25, unique=True, default='')
    description = models.CharField(max_length=50, null=False)
    #description = models.CharField(max_length=25, default='')
    #views = models.IntegerField(default=0)
    #likes = models.IntegerField(default=0)
    #slug = models.SlugField(default='', unique=True)

    def __str__(self):
        return self.name

class Category(models.Model):
    super_category = models.ForeignKey(Super_category)
    name = models.CharField(max_length=30, unique=True)
    description = models.CharField(max_length=50, null=False)
    #views = models.IntegerField(default=0)
    #likes = models.IntegerField(default=0)
    #slug = models.SlugField(default='', unique=True)


    def __str__(self):
        call = self.name + '    ---->    ' +  self.super_category.name
        return call

class Page(models.Model):
    category = models.ForeignKey(Category)
    postby = models.ForeignKey(User)
    title = models.CharField(max_length=50)
    data = models.TextField()
    views = models.IntegerField(default=0)
    date = models.DateTimeField(default=datetime.now())
    like = models.IntegerField(default=0)
    tags = TagAutocompleteField(null=True, blank=True, )
    #slug = models.SlugField(default='', unique=True)

    def __str__(self):
        return self.title

class Comment(models.Model):
    page = models.ForeignKey(Page)
    data = models.TextField()
    postby = models.ForeignKey(User)
    date = models.DateTimeField(default=datetime.now())
    like = models.IntegerField(default=0)
    #slug = models.SlugField(default='', unique=True)
    #name = "page= " + page + " comment=" + data[:30]

    def __str__(self):
        x = self.page
        z = self.data[:30]
        y = "page= " + str(x) + " comment= " + z
        return y

class LikeComment(models.Model):
    user = models.ForeignKey(User)
    comment = models.ForeignKey(Comment)

    def __str__(self):
        id = str(self.id)
        return id


class LikePage(models.Model):
    user = models.ForeignKey(User)
    page = models.ForeignKey(Page)

    def __str__(self):
        id = str(self.id)
        return id


class Document(models.Model):
    docfile = models.FileField(upload_to='documents/%Y/%m/%d')
    date = models.DateTimeField(default=datetime.now())
    postby = models.ForeignKey(User)

    def __str__(self):
        #id = str(self.id)
        return self.docfile.url