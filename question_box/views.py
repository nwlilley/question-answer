from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.conf.urls.static import static
from .models import Question, Answer
from .forms import QuestionForm
from django.http import JsonResponse
import json
from django.views.decorators.csrf import csrf_exempt




# Create your views here.

def question_list(request):
    questions = Question.objects.all()
    return render(request, 'questions.html', {'questions':questions})

def question_detail(request, pk):
    question = get_object_or_404(Question, pk=pk)
    return render(request, 'question_detail.html', { 'question':question, 'pk':pk })

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('questions.html')
    else:
        form = UserCreationForm()
    return render(request, 'registration.html', {'form': form})

def user_profile(request):
    questions = Question.objects.filter(user=request.user)
    # if request.method == "POST":
    #     form = QuestionForm(request.POST)
    #     question_pk = request.POST.get('question')
    #     question = Question.objects.get(pk=question_pk)
    #     form.save()
        # value_entry = request.POST.get('value_entry')
        # log = Log.objects.create(habit=habit, value_entry=value_entry)
        
    # form = QuestionForm()
    return render(request, 'questions.html', {'questions': questions})

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

def add_answer(request):
    data = json.loads(request.body.decode("utf-8"))
    answer = data.get('answer')
    new_answer = Answer.objects.create(answer=answer)
    return JsonResponse({
        "status": "ok",
        "data": {
            "pk": new_answer.pk,
            "answer": new_answer.answer,
        }
    })