from django.contrib import admin

# Register your models here.

# Calling models
from .models import Topic, Answer

# Adding model

admin.site.register(Topic)
admin.site.register(Answer)