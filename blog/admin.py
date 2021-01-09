from django.contrib import admin

# Register your models here.
from .models import Blogpost, Contact, Category, Author, Comment

@admin.register(Blogpost)
class BlogpostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'author','status', 'created_on')
    list_filter = ('author', 'status')
    search_fields = ('title', 'content')
    prepopulated_fields = {'slug': ('title',)}

    class Media:
        js = ('blog/js/tiny.js',)




admin.site.register(Contact)
admin.site.register(Author)
admin.site.register(Category)
admin.site.register(Comment)