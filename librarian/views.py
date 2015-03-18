from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import logout
# from polls.models import Question,Choice
from django.core.urlresolvers import reverse

@login_required(login_url='/librarian/login/')
def index(request):
	return HttpResponse('You are logged in ')

@login_required(login_url='/librarian/login/')
def first(request):
	return HttpResponse("vivek yeah")

def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('librarian:index'))