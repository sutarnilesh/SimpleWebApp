from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

# Create your views here.
def my_view(request):
    #import pdb;pdb.set_trace()
    context = dict()
    #if request.user.username:
    username = request.user.username
    template = loader.get_template("../templates/home.html")
    msg = "Hello World!"
    context = {'user': request.user, 'massage': msg}
    return HttpResponse(template.render(context, request))
#    else:
#        template = loader.get_template("../templates/login.html")
#        return HttpResponse(template.render(context, request))

