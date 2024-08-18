from django.contrib import admin
from .models import Article, Mail

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'date')  # Display these fields in the admin panel

@admin.register(Mail)
class MailAdmin(admin.ModelAdmin):
    list_display = ('text', 'date')  # Display these fields in the admin panel
