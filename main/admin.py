from django.contrib import admin
from .models import Tutorials
from tinymce.widgets import TinyMCE
from django.db import models

class TutorialsAdmin(admin.ModelAdmin):
    fieldsets=[
        ("Title/date",{"fields":["tutorial_title","tutorial_published"]}),
        ("Contents",{"fields":["tutorial_content"]})
    ]
    formfield_overrides={
        models.TextField:{'widget':TinyMCE()}
    }

# Register your models here.
admin.site.register(Tutorials, TutorialsAdmin)