from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.shortcuts import get_object_or_404, render
from django.urls import reverse

from .models import Question, Choice

def index(request):
    latest_question_list = Question.objects.order_by("-publication_date")[:5]
    template = loader.get_template("polls/index.html")
    context = {
        "latest_question_list": latest_question_list,
    }
    return HttpResponse(template.render(context, request))

def detail(request, question_id):
    question = get_object_or_404(Question, pk = question_id)
    return render(request, "polls/detail.html",{"question":question})

def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, "polls/results.html", {"question": question})

def model_result(request):
    latest_question_result = Question.objects.order_by("-publication_date")
    output = "<ol> <li>"+ str("</li> <li>".join([q.question_text for q in latest_question_result]))+"</li>"
    return HttpResponse(output)


def vote(request, question_id):
    




