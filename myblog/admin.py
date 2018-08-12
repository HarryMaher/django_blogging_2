from django.contrib import admin
from myblog.models import Post
from myblog.models import Category


admin.site.register(Category)

# Category selector inside of posts
class CategoriesInLine(admin.TabularInline):
    model = Category.posts.through

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    inlines = [
        CategoriesInLine,
    ]
# exclude post selector from admin catogires
# https://docs.djangoproject.com/en/2.1/ref/contrib/admin/

class CategoryAdmin(admin.ModelAdmin):
	exclude = 'posts'

# admin.site.register(Post)
