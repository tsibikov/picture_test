from django.db import models


class Question(models.Model):
    ''' Модель вопроса '''
    question_text = models.TextField() # текст вопроса
    answer_a = models.URLField() # вариант ответа A
    answer_b = models.URLField() # вариант ответа B
    answer_c = models.URLField() # вариант ответа C
    answer_d = models.URLField() # вариант ответа D
    is_right = models.CharField(max_length=1) # Правильный ответ


class Quiz(models.Model):
    ''' Модель прохождения теста '''
    id = models.AutoField(primary_key=True, unique=True) #id теста
    questions_count = models.IntegerField(verbose_name='Количество вопросов') # количество вопросов в тесте
    score = models.IntegerField(verbose_name='Оценка теста') # Оценка прохождения теста


    def __str__(self):
        return f"{self.id, self.questions_count, self.score}"