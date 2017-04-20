from django.contrib import admin
from knowledge_management.models import Category, Page, Super_category, Comment, LikeComment,  Document, LikePage

#class CategoryAdmin(admin.ModelAdmin):
   # prepopulated_fields = {'slug':('name', )}

#class PageAdmin(admin.ModelAdmin):
    #prepopulated_page = {'slug':('title', )}

# Update the registeration to include this customised interface

admin.site.register(Super_category)
admin.site.register(Category)
admin.site.register(Page)
admin.site.register(Comment)
admin.site.register(LikeComment)
admin.site.register(Document)
admin.site.register(LikePage)


