from django.shortcuts import render
from django.http import HttpResponse
from .models import Question
# Create your views here.

def index(request):
    question_list = Question.objects.order_by('-pub_date')
    output = ""
    for q in question_list:
        output += q.question_text
        output += ', '

    return HttpResponse(output)

    return HttpResponse("hehehehe")
    

def detail(request, question_id):  
    return HttpResponse("문제보기: {}".format(question_id))


def result(request, question_id):
    return HttpResponse("문제 결과: {}".format(question_id))


def vote(request, question_id):
    return HttpResponse("내가 한 투표: {}".format(question_id))

