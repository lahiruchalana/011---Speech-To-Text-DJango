from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse

# Create your views here.

def hello(firstname) :
    name = firstname

    return name

def hi(request) :
      template = loader.get_template('SpeechToTextApp/hi.html')
      firstname = 'lahiru'
      helloFirstName = hello(firstname)

      context = {
        'name': 'Linus',
        'firstname': helloFirstName,
      }

      return HttpResponse(template.render(context, request))
