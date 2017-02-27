from django.db import models
from django.utils import timezone

# Create your models here.

class Request(models.Model):
	student = models.ForeignKey('People.Student')
	course = models.ForeignKey('Courses.Course')
	request_rank = models.IntegerField() # 0 is best

	created_at = models.DateField(default=timezone.now)

	def __str__(self):
		return '%s\'s request for %s (%s)' % (self.student.full_name(), self.course.display_name, self.request_rank)

class Placement(models.Model):
	student = models.ForeignKey('People.Student')
	course = models.ForeignKey('Courses.Course')
	leader = models.BooleanField(default=False)

	created_at = models.DateField(default=timezone.now)

	def __str__(self):
		return '%s\'s placement in %s' % (self.student.full_name(), self.course.display_name)
