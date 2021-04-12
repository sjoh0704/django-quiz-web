from django.shortcuts import render,redirect
from django.http import HttpResponse, Http404
from .models import Question, Choice

# Create your views here.

def index(request):
    question_list = Question.objects.order_by('-pub_date')
    context = {'latest_question_list': question_list}
    return render(request, 'index.html', context)

    

def detail(request, question_id): 
    try:
        question = Question.objects.get(pk=question_id)
        # choice = Choice.objects.get(pk=question_id)

    except Question.DoesNotExist:
        raise  Http404("Question Does not Exist")

    return render(request, 'detail.html', {"question":question})

def result(request, question_id):
    return HttpResponse("문제 결과: {}".format(question_id))


def vote(request, question_id):
    question = Question.objects.get(pk=question_id)

    try:
        # print(request.POST['choice'])
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
        
        
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'detail.html', {
            'error_message':"초이스를 선택하지 않았음",
            'question': question
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()

    return redirect('/polls/{}/results'.format(question_id))
