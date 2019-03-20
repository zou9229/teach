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
        return '%s' % self.classname
        pass


class studentinformation(models.Model):
	SEX = (
		('male', '男'),
		('feamale', '女')
	)
	stunumber = models.CharField(max_length=10,primary_key=True)
	stuname = models.CharField(max_length=10)
	stusex = models.CharField(max_length=8,choices=SEX)
	stuage = models.IntegerField(max_length=18)
	stuAcademy = models.CharField(max_length=15)
	stuIDcard = models.CharField(max_length=18,unique=True)
	create = models.DateTimeField(auto_now_add=True)
	login = models.DateTimeField(auto_now=True)
	def __str__(self):
		return ' %s' % self.stunumber
		pass


class grademanage(models.Model):
	stunumber = models.CharField(max_length=10)
	stunumber = models.ForeignKey(studentinformation,on_delete=models.CASCADE)
	stuname = models.CharField(max_length=10)
	classnumber = models.CharField(max_length=10)
	classnumber = models.ForeignKey(classmanage,on_delete=models.CASCADE)
	classname = models.CharField(max_length=10)
	normalgrade = models.IntegerField(max_length=3)
	testgrade = models.CharField(max_length=3)

	class Meta:
		unique_together = ("stunumber", "classnumber")

	def __str__(self):
		return 'grademanage : %s' % self.classnumber
		pass

class users(models.Model):
	SEX = (
		('male','男'),
		('feamale','女')
		)
	id = models.AutoField(primary_key=True)
	username = models.CharField(max_length=10)
	password = models.CharField(max_length=128)
	sex = models.CharField(max_length=8,choices=SEX)
	age = models.IntegerField(max_length=18)
	img = models.ImageField(upload_to='static/img/img',null=True)
	name = models.CharField(max_length=50,null=True)
	create = models.DateTimeField(auto_now_add=True)
	login = models.DateTimeField(auto_now=True)

	def __str__(self):
		return 'user : %s' % self.username
		pass


class userteach(models.Model):
	classnumber = models.CharField(max_length=18,primary_key=True)
	classnumber = models.ForeignKey(classmanage, on_delete=models.CASCADE)
	classname = models.CharField(max_length=18)
	classdata = models.CharField(max_length=18)
	classAcademy = models.CharField(max_length=18)
	create = models.DateTimeField(auto_now_add=True)
	login = models.DateTimeField(auto_now=True)