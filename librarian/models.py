from django.db import models

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

class 
