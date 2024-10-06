from django.contrib import admin

from .models import Post,UserProfile,ThreadModel,MessageModel,Notification

# Register your models here.

admin.site.register(Post)
admin.site.register(UserProfile)
admin.site.register(ThreadModel)
admin.site.register(MessageModel)
admin.site.register(Notification)
