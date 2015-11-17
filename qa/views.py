from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Question, Answer

class QuestionsList(ListView):
    template_name='qa/questions_list.html'
    model = Question
