from django.db import models

class User(models.Model):
    userid = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=64)
    roll_number = models.CharField(unique=True, max_length=10, blank=True)
    registration_number = models.CharField(unique=True, max_length=10, blank=True)
    current_section = models.CharField(max_length=4)
    current_year = models.CharField(max_length=4)
    joining_year = models.CharField(max_length=4)
    course = models.CharField(max_length=10)
    branch = models.CharField(max_length=10)
    gender = models.CharField(max_length=1)
    email = models.CharField(unique=True, max_length=64)
    birthday = models.DateField()
    country = models.CharField(max_length=32)
    mobile = models.CharField(max_length=16)
    emergency_contact = models.CharField(max_length=16)
    sbh_account = models.CharField(max_length=32, blank=True)
    passport = models.CharField(max_length=20, blank=True)
    hostel_room = models.CharField(max_length=10)
    hostel = models.CharField(max_length=10)
    mess = models.CharField(max_length=10)
    created_location = models.CharField(max_length=32)
    created_time = models.DateTimeField()


class Publisher(models.Model):
	pubid=models.IntegerField(primary_key=True)
	name=models.CharField(max_length=100)
	def __unicode__(self):
		return self.pubid+" "+self.name

class Book(models.Model):
	bookid=models.IntegerField(primary_key=True)
	accno=models.IntegerField()
	classno=models.CharField(max_length=100)
	bookno=models.CharField(max_length=100)
	name=models.CharField(max_length=100)
	no_copies=models.IntegerField()
	pubid=models.ForeignKey(Publisher)
	def __unicode__(self):
		return self.bookid+" "+self.bname

class Author(models.Model):
	authorid=models.IntegerField(primary_key=True)
	name=models.CharField(max_length=100)
	def __unicode__(self):
		return self.authorid+" "+self.name

class bookauthor(models.Model):
	bookid=models.ForeignKey(Book)
	authorid=models.ForeignKey(Author)
	def __unicode__(self):
		return self.bookid

class Issue(models.Model):
	userid=models.ForeignKey(User)
	bookid=models.ForeignKey(Book)
	issue_date=models.DateField()
	due_date=models.DateField()
	def __unicode__(self):
		return self.userid+" "+self.bookid
    


    

