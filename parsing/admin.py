from django.contrib import admin

from parsing.models import News

admin.site.register(News)

# @admin.register(News)
# class NewsAdmin(admin.ModelAdmin):
#     list_display = (
#         "id",
#         "title",
#         "datetime",
#         "tags",
#     )
#     search_fields = ("datetime", "tags")
#     empty_value_display = "-пусто-"
