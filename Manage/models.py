from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Module(models.Model):
	name = models.CharField(max_length=30)
	description = models.TextField(max_length=1000)
	def __str__(self):
		if len(self.description) < 50:
			return ("{} - {}".format(self.name,self.description))
		else:
			return ("{} - {}".format(self.name,self.description[50:] + "..."))


class Trainer(models.Model):
	name = models.CharField(max_length=30)
	lastname = models.CharField(max_length=30)
	birthday = models.DateField()	
	email = models.CharField(max_length=30)
	phoneNumber = models.CharField(max_length=30)
	wage = models.IntegerField()
	def __str__(self):
		return ("{} {}".format(self.name,self.lastname))

class Training(models.Model):
	trainer = models.ForeignKey(Trainer,on_delete = models.CASCADE)
	module = models.ForeignKey(Module,on_delete = models.CASCADE)
	opened = models.DateField()
	closed = models.DateField()
	price = models.IntegerField()
	def __str__(self):
		return ("{} - {}".format(self.trainer,self.module))	

class Group(models.Model):
	name = models.CharField(max_length=30)
	opened = models.DateField()
	closed = models.DateField()
	training = models.ForeignKey(Training,on_delete = models.CASCADE)
	def __str__(self):
		return self.name

class Student(models.Model):
	user = models.OneToOneField(User,on_delete = models.CASCADE)
	name = models.CharField(max_length=30)
	lastname = models.CharField(max_length=30)
	birthday = models.DateField()
	group = models.ForeignKey(Group,on_delete = models.CASCADE)
	email = models.CharField(max_length=50)
	parentsNumber = models.CharField(max_length=30)
	def __str__(self):
		return ("{} {}".format(self.name,self.lastname))

class Event(models.Model):
	name = models.CharField(max_length=30)
	opened = models.DateField()
	closed = models.DateField()
	description = models.TextField(max_length=1000)
	price = models.IntegerField()
	def __str__(self):
		return ("{} - {}".format(self.opened,self.name))

class Payment(models.Model):
	firstName = models.CharField(max_length=30)
	lastName = models.CharField(max_length=30)
	student = models.ForeignKey(Student,on_delete = models.CASCADE)
	group = models.ForeignKey(Group,on_delete = models.CASCADE)
	status = models.CharField(max_length=1, blank=True, default='W', choices=(('W', 'Waiting for payment'),('P', 'Payment complete')))
	due_date = models.DateField(blank=True,default="")
	complete = models.DateField(blank=True,default="")

	def __str__(self):
		return("#{} - {} {}".format(self.id,self.firstName,self.lastName))