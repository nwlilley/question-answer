from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.conf.urls.static import static
from django.utils import timezone
from .models import Question, Answer
from .forms import AnswerForm
from django.http import JsonResponse
import json
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required




# Create your views here.

def question_list(request):
    questions = Question.objects.all().order_by('-created_at')
    return render(request, 'questions.html',
    # change context to something json objects
    # template tag for json called {% to json %} or something
    {'questions':questions})

# def question_list(request):
#     questions = Question.objects.all()

#     return JsonResponse({
#         "status": "ok",
#         "data": {
#             "pk": questions.pk,
#             "title": questions.title,
#             "body": questions.body,
#         }
#     }
#     )

@login_required
def question_detail(request, pk):
    question = get_object_or_404(Question, pk=pk)
    answers = Answer.objects.filter(answer=question.pk).order_by('-added_at')
    if request.method == "POST":
        form = AnswerForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.answer = question
            post.user = request.user
            post.added_at = timezone.now()
            post.save()
            return redirect('question-detail', pk=pk)
    else: 
        form = AnswerForm()
    return render(request, 'question_detail.html', { 'question':question, 'pk':pk, 'answers': answers, 'form': form})

# def signup(request):
#     if request.method == 'POST':
#         form = UserCreationForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('questions.html')
#     else:
#         form = UserCreationForm()
#     return render(request, 'registration.html', {'form': form})

def user_profile(request):
    # questions = Question.objects.filter(user=request.user)
    questions = Question.objects.all().order_by('-created_at')
    return render(request, 'questions.html', {'questions': questions})

def user_questions(request):
    questions = Question.objects.filter(user=request.user)
    return render(request, 'user_questions.html', {'questions': questions})

@csrf_exempt
def new_question(request):
    data = json.loads(request.body.decode("utf-8"))
    question_title = data.get('title')
    question_body = data.get('body')
    new_question = Question.objects.create(title=question_title, body=question_body,)
    return JsonResponse({
        "status": "ok",
        "data": {
            "pk": new_question.pk,
            "title": new_question.title,
            "body": new_question.body,
        }
    })

@csrf_exempt
def add_answer(request, pk):
    answer = get_object_or_404(Answer, pk=pk)
    if request.method == "POST":
        form = AnswerForm(request.POST)
        answer = request.POST.get('answer')
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.added_at = timezone.now()
            post.save()
            return redirect('question-detail', pk=pk)
    else:
        form = AnswerForm()
    return render(request, 'question_detail.html', {'form':form},)

    # data = json.loads(request.body.decode("utf-8"))
    # answer = data.get('answer')
    # new_answer = Answer.objects.create(answer=answer)
    # return JsonResponse({
    #     "status": "ok",
    #     "data": {
    #         "pk": new_answer.pk,
    #         "answer": new_answer.answer,
    #     }
    # })
