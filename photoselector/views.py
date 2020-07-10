from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from django.template import loader

def index(request):
    template = loader.get_template('photoselector/index.html')
    context = {
        #'latest_question_list': latest_question_list,
    }
    return HttpResponse(template.render(context,request))
