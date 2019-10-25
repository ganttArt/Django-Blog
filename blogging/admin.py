from django.contrib import admin
from blogging.models import Post, Category

# lesson 7, assignment
class CategoryInline(admin.TabularInline):
    model = Category.posts.through


class PostAdmin(admin.ModelAdmin):
    inlines = [CategoryInline,]


class CategoryAdmin(admin.ModelAdmin):
    # this eliminates posts from the category admin page
    exclude = ('posts',)

    # # this would add the ability to change the post's categories
    # # on the categories admin page, but we dont want that
    # inlines = [CategoryInline,]


admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)
