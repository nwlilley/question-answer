from django.shortcuts import render, redirect, get_object_or_404
from django.conf.urls.static import static
from .models import Question


# Create your views here.

def question_list(request):
    questions = Question.objects.all()
    return render(request, 'questions.html', {'questions':questions})

def question_detail(request, pk):
    question = get_object_or_404(Question, pk=pk)
    return render(request, 'question_detail.html', { 'question':question, 'pk':pk })
