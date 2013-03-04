# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext
from django.shortcuts import render_to_response
from admitDB.models import University, Student
from admitDB.forms import studentForm

def home(request):
  return render_to_response('index.html')

def getUniversityList(request):
    """Returns the list of all universities in the database"""
    universities = University.objects.all().values('univ_name','univ_city','univ_website')
    return render_to_response('univ_list.html', {'universities':universities})

def showAddStudent(request):	
    return render_to_response('student.html')
	
def addStudent(request):
  if request.method == 'POST':
    form = studentForm(request.POST)
    if form.is_valid():
      studentData = form.cleaned_data
      student = Student(name=studentData['name'], BITS_ID=studentData['BITS_ID'], email=studentData['email'], password=studentData['password'])
      student.save()
      return HttpResponseRedirect('/thanks')
    else:
      return render_to_response('student.html',{'form' : form, 'error': form.errors }, RequestContext(request))
  else:
    form = studentForm()
    return render_to_response('student.html', {'form': form}, RequestContext(request))

def thanksPage(request):
  return render_to_response('thanks.html')
