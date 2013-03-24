from django.db import models
from django.core.validators import URLValidator
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User, UserManager
from django.db.models.signals import post_save

# Create your models here.
class University(models.Model):
	"""University class
		:Parameters:
			- 
		To add column	
	"""
	univ_ID = models.AutoField(primary_key=True)
	univ_name = models.CharField("University Name", max_length=100)
	univ_city = models.CharField("City", max_length=30)
	univ_state = models.CharField("State", max_length=30, null=True)
	univ_country = models.CharField("Country", max_length=20)
	univ_website = models.URLField("URL")
		
	def getUniversityNameURL(self):
		return University.objects.all.values_list('univ_name','univ_city','univ_website')
	
	def addUniversity(self, u_name, u_city, u_country, u_website, u_state=None):
		"""To add a university in the database.
    	:param u_name: University name
    	:param u_city: University city
    	:param u_country: University country
    	:param u_website: University URL. Should start with http://
    	:param u_state: University state. (optional, default: None)
    	:type name: str.
    	:type state: bool.
    	:returns:  Nothing.
    	:raises: ValidationError	
    	"""
		isURLValid = URLValidator(verify_exists=False)
		try:
			isURLValid(u_website)
		except ValidationError as e:
			print u'URL %s is not valid: URLs should start with http://' % (u_website)
		else:
			universityRow = University(univ_name=u_name, univ_city=u_city, univ_state=u_state, univ_country=u_country, univ_website=u_website)
			universityRow.save()
	
	def __unicode__(self):
		return u'%s, %s' %(self.univ_name, self.univ_city)
	

class Student(models.Model):
    # you get a 'student_id' column because of this. 
    # We will use this as a primary key.
    student_ID = models.OneToOneField('auth.User', unique = True, primary_key = True)
    #name = models.CharField("First Name", max_length=30)
    BITS_ID = models.CharField("BITS ID", max_length=12)
    #student_campus = (('P', 'Pilani'), ('G', 'Goa'), ('D', 'Dubai'),('H', 'Hyderabad'),	)
    #email = models.CharField("Email ID", max_length=40, unique=True)
    def __unicode__(self):
        return u'%s' %(self.name)
    
    def getBITSID(self):
        return u'%s' %(self.BITS_ID)


		
class Student_Info(models.Model):
	student_ID = models.ForeignKey(Student, primary_key=True)
	discipline = models.CharField("Discipline", max_length=2)#dictionary object for code to name matching of discipline
	target_discipline = models.CharField("Discipline for Graduate studies", max_length=2)
	sub_area = models.CharField("Area of Specialization", max_length=20, null=True)
	cgpa = models.FloatField("CGPA")
	gre_verbal = models.IntegerField("Verbal score", null=True)
	gre_quant = models.IntegerField("Quant score", null=True)
	gre_essay = models.FloatField("Essay score", null=True)
	toefl_total = models.IntegerField("TOEFL total score",null=True)
	toefl_speaking = models.IntegerField("TOEFL speaking score",null=True)
	
class Application_Info(models.Model):
	student_IDs = models.ForeignKey(Student)
	applied_cycle = models.CharField(max_length=1, default='F')#F for fall S for Spring
	applied_year = models.PositiveIntegerField("Applied for year", max_length=4)
	univ_IDs = models.ForeignKey(University)
	degree_applied_to = models.CharField(max_length=1, default='P')#M for Masters, P for PhD
	admitted = models.NullBooleanField("Got Admit?")
		
	class Meta:
		unique_together = ('student_IDs','univ_IDs','applied_year')

class Work_Info(models.Model):
	student_ID = models.ForeignKey(Student)
	number_of_years = models.PositiveSmallIntegerField()#default in PS1/PS2/TS
	work_type = models.CharField(max_length=10)#Job/PS2/PS1/TS/Internship
	organization_name = models.CharField(max_length=50)#Organization name, city, country
	applied_with_experience = models.BooleanField()
	work_nature = models.CharField(max_length=20, null=True)#Research/Development/Consultancy
