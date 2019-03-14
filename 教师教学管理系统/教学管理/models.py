from django.db import models

# Create your models here.

class grademanage(models.Model):
    classnumber = models.CharField(max_length=10,unique=True)
    classname = models.CharField(max_length=10,unique=True)
    classteacher = models.CharField(max_length=5)
    classgrade = models.IntegerField(max_length=3)
    classAcademy = models.CharField(max_length=15)
    classintroduce = models.CharField(max_length=60)

    def __str__(self):
        return 'grademanage : %s' % self.classname