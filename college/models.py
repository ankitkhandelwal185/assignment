# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Date(models.Model):
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at= models.DateTimeField(auto_now=True,null=True)

	class Meta:
		abstract = True

class College(Date):
    college_name = models.CharField(max_length=100)
    avg_pkg = models.CharField(max_length=20)
    rank =models.IntegerField(default=0)

    def __str__(self):
        return self.college_name

class Course(Date):
    course_name = models.CharField(max_length=50)
    avg_fees = models.CharField(max_length=25)
    college = models.ForeignKey(College, related_name='college_course', on_delete=models.CASCADE)

    def __str__(self):
        return self.course_name, self.college
