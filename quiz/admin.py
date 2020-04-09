from django.contrib import admin

from .models import Question, Quiz, Attempted

admin.site.register(Attempted)
admin.site.register(Question)
admin.site.register(Quiz)
