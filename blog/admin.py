from django.contrib import admin

from blog.models import Post,Category


#@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    date_hierarchy = "created_date"
    #empty_value_display='_empty_'
    #fields=('title',)
    list_display=('title','author','id','counted_views','status','published_date','created_date')
    list_filter=('status','counted_views','author')
    search_fields=('content','title')
admin.site.register(Category)    
admin.site.register(Post,PostAdmin)
