from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Tweet

# この関数を編集した

def kanri(request):
    return render(request, 'kanri.html')

def post(request):
    item = request.POST['item']
    tweet = Tweet(item=item)
    tweet.save()
    return HttpResponseRedirect(reverse('tweets:kanri'))

def item(request):
    item = Tweet.objects.all()
    context = {'item':item}
    template = loader.get_template('view.html')
    return HttpResponse(template.render(context,request))