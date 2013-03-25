# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User
from django.forms.util import ErrorList
from django.core.exceptions import ValidationError
from django.template import RequestContext
from django.shortcuts import render_to_response
from admitDB.models import University, Student, Student_Info
from admitDB.forms import studentRegisterForm, studentInfoForm
from django.contrib import auth
from django.db.models import signals
from django.contrib.auth.decorators import login_required


@login_required
def home(request):
  return render_to_response('index.html')

def getUniversityList(request):
    """Returns the list of all universities in the database"""
    universities = University.objects.all().values('univ_name','univ_city','univ_website')
    return render_to_response('univ_list.html', {'universities':universities})

def showAddStudent(request):
    return render_to_response('student_register.html')

#def register(request, success_url=None, form_class=RegistrationForm, profile_callback=None, template_name='registration/registration_form.html', extra_context=None):#
#	return

def addStudent(request):
    if request.method == 'POST':
        form = studentRegisterForm(request.POST)
        if form.is_valid():
            studentData = form.cleaned_data
            try:
                Student.objects.get(BITS_ID=studentData['BITS_ID'])
            except Student.DoesNotExist:
                student = User.objects.create_user(username=form.cleaned_data['email'],
                                        password=form.cleaned_data['password'],
                                        email=form.cleaned_data['email']               
                                        )
                student.first_name = form.cleaned_data['first_name']
                student.last_name = form.cleaned_data['last_name'] 
                # student.save()
                
                student_profile = student.profile
                student_profile.BITS_ID = form.cleaned_data['BITS_ID']
                student_profile.save()
                print "ONE"
                #student.is_active = True
                return HttpResponseRedirect('/thanks')
            else:
                form.errors['email'] = ErrorList([u'Email address already exists'])
                return render_to_response('student_register.html', {'form' : form, 'error': form.errors }, RequestContext(request))
        else:
            return render_to_response('student_register.html', {'form' : form, 'error': form.errors }, RequestContext(request))
    else:
        form = studentRegisterForm()
        return render_to_response('student_register.html', {'form': form}, RequestContext(request))

def create_user_profile(sender, instance, created, **kwargs):  
    if created:  
        print "TWO"
        profile, created = Student.objects.get_or_create(student_ID=instance) 
        print "THREE"

signals.post_save.connect(create_user_profile, sender=User) 

User.profile = property(lambda u: Student.objects.get_or_create(student_ID=u)[0])

def thanksPage(request):
    return render_to_response('thanks.html')

@login_required
def addStudentInfo(request):
    if request.method == 'POST':
        form = studentInfoForm(request.POST)
        if form.is_valid():
            studentInfoData = form.cleaned_data
            # TODO: try except block is incomplete. We need to check it against a session. 
            # There is no unique entry in this form to check if a corresponding entry 
            # existed earlier. 
            student_info = Student_Info(student_id = request.session['user_id'], 
                                        target_discipline = studentInfoData['target_discipline'],
                                        sub_area = studentInfoData['sub_area'],
                                        cgpa = studentInfoData['cgpa'],
                                        gre_verbal = studentInfoData['gre_verbal'],
                                        gre_quant = studentInfoData['gre_quant'],
                                        gre_essay = studentInfoData['gre_essay'],
                                        toefl_total = studentInfoData['toefl_total'],
                                        toefl_speaking = studentInfoData['toefl_speaking'] )
            student_info.save()
            return HttpResponseRedirect('/thanks')
        else:
            return render_to_response('student_info.html', {'form': form , 'error':form.errors}, RequestContext(request))
    else:
        form = studentInfoForm()
        return render_to_response('student_info.html', {'form': form}, RequestContext(request))


def verifyLogin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None and user.is_active:
            # Correct password, and the user is marked "active"
            auth.login(request, user)
            # Redirect to a home page. 
            #TODO: The redirection should be to a page 
            #from where the user was redirected to login ideally.
            request.session['user_id'] = user.id
            print request.session['user_id']
            return HttpResponseRedirect("/")
        else:
            # Render the login page again. Show error though
            return render_to_response("registration/login.html", {'invalid': True}, RequestContext(request))
    else:
        return render_to_response("registration/login.html", {'invalid': False}, RequestContext(request))
    
def logout(request):
    auth.logout(request)
    return render_to_response("registration/login.html", {'logged_out': True}, RequestContext(request))

def StudentAuthModelBackend(): 
    u = User.objects.get(pk=1) # Get the first user in the system
    user_id = u.get_profile().BITS_ID
    return user_id
                
