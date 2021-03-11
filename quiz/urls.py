from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('quiz/<int:quiz_id>/<int:question_id>/<int:prew_question_id>', views.quiz, name='quiz'),
    path('result/<int:quiz_id>/<int:prew_question_id>', views.result, name='result')
]