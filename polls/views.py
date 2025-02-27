from django.http import HttpResponse, HttpRequest, Http404
from .models import Question
from django.shortcuts import render, get_object_or_404
from django.template import loader


def index(request: HttpRequest):
    latest_question_list = Question.objects.order_by("-pub_date")[:5]
    context = {"latest_question_list": latest_question_list}
    return render(request, "polls/index.html", context)


def detail(request: HttpRequest, question_id: int):
    q = get_object_or_404(Question, pk=question_id)
    return render(request, "polls/detail.html", {"question": q})


def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)


def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)
