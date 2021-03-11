from django.contrib import admin
from .models import Question, Quiz



class QuestionAdmin(admin.ModelAdmin):
    list_display = ("id", "question_text", "answer_a", "answer_b", "answer_c", "answer_d", "is_right",) 
    empty_value_display = "-пусто-"  


class QuizAdmin(admin.ModelAdmin):
    list_display = ("id", "questions_count", "score",) 
    empty_value_display = "-пусто-"  

admin.site.register(Question, QuestionAdmin)    
admin.site.register(Quiz, QuizAdmin)  

