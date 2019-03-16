from django.db import models

# Create your models here.

class classmanage(models.Model):
    classnumber = models.CharField(max_length=10,primary_key=True)
    classname = models.CharField(max_length=10,unique=True)
    classteacher = models.CharField(max_length=5)
    classgrade = models.IntegerField(max_length=3)
    classAcademy = models.CharField(max_length=15)
    classintroduce = models.CharField(max_length=60)

    def __str__(self):
        return 'classmanage : %s' % self.classname
        pass


class grademanage(models.Model):
	stunumber = models.CharField(max_length=10)
	stuname = models.CharField(max_length=10)
	classnumber = models.CharField(max_length=20)
	classnumber = models.ForeignKey(classmanage,on_delete=models.CASCADE)
	normalgrade = models.IntegerField(max_length=3)
	testgrade = models.CharField(max_length=3)

	class Meta:
		unique_together = ("stunumber", "classnumber")

	def __str__(self):
		return 'grademanage : %s' % self.stuname
		pass

class users(models.Model):
	SEX = (
		('male','男'),
		('feamale','女')
		)
	username = models.CharField(max_length=10)
	password = models.CharField(max_length=128)
	sex = models.CharField(max_length=8,choices=SEX)
	age = models.IntegerField(max_length=18)
	create = models.DateTimeField(auto_now_add=True)
	login = models.DateTimeField(auto_now=True)

	def __str__(self):
		return 'user : %s' % self.username
		pass