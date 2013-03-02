# Create your views here.

from django.http import HttpResponse
from django.shortcuts import render_to_response
from admitDB.models import University

def univ_list(request):
	universities = University.objects.all()
	return render_to_response('univ_list.html', {'universities':universities})

