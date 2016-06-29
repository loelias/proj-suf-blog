from django.contrib import admin
from blog.models.post import Post
from blog.models.comentario import Comentario

# Register your models here.
admin.site.register(Post)
admin.site.register(Comentario)
