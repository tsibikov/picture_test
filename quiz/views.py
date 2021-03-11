from django.shortcuts import render
from .models import Question, Quiz


def index(request):
    """ Главная страница """
    question_id = Question.objects.all().first().id
    questions = Question.objects.all()
    questions_count = len(questions)
    quiz = Quiz.objects.create(questions_count=questions_count,
                               score=0)
    prew_question_id = 0
    return render(request, 'index.html',{'quiz_id': quiz.id, 
                                        'question_id': question_id,
                                        'prew_question_id': prew_question_id,
                                        'questions_count': questions_count}) 


def quiz(request, quiz_id, question_id, prew_question_id):
    """ Тест """
    question = Question.objects.get(id=question_id)
    quiz = Quiz.objects.get(id=quiz_id)
    try:
        question_id = Question.objects.filter(id__gt=question_id)[0].id
    except:
        question_id = 'finish'
    if 'answer' in request.GET:
        answer = request.GET['answer']
        prew_question = Question.objects.get(id=prew_question_id)
        if answer == prew_question.is_right:
            quiz.score += 1
            quiz.save()
        prew_question_id = question.id
        return render(request, 'quiz.html',{'question': question, 
                                            'question_id': question_id, 
                                            'quiz_id': quiz_id, 
                                            'prew_question_id': prew_question_id})
    prew_question_id = question.id
    return render(request, 'quiz.html',{'question': question, 
                                        'question_id': question_id, 
                                        'quiz_id': quiz_id, 
                                        'prew_question_id': prew_question_id})   


def result(request, quiz_id, prew_question_id):
    """ Результат теста """
    quiz = Quiz.objects.get(id=quiz_id)
    if 'answer' in request.GET:
        answer = request.GET['answer']
        prew_question = Question.objects.get(id=prew_question_id)
        if answer == prew_question.is_right:
            quiz.score += 1
            quiz.save()
    result_scores = int(quiz.score / (quiz.questions_count / 100))
    return render(request, 'result.html',{'result_scores': result_scores})