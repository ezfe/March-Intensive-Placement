from django.db import models
import uuid
import re
from Registrations.models import Placement

def generateUUID():
    return str(uuid.uuid4())

# Create your models here.

class Course(models.Model):
    course_id = models.CharField(max_length=36,unique=True,primary_key=True,default=generateUUID)
    display_name = models.CharField(max_length=200)
    course_type = models.CharField(max_length=8,default='FULL',choices=[('FULL', 'Full Day'), ('AM', 'Morning'), ('PM', 'Afternoon')])
    max_students = models.IntegerField(default=0)
    is_travel = models.BooleanField(default=False, verbose_name="travel")
    cost = models.FloatField(default=0.0)
    room = models.CharField(max_length=50,default='')

    manual_placement = models.BooleanField(default=False, verbose_name="manual placement")

    def number_female(self):
        c = 0
        for student in self.student_list():
            if student.gender == "F":
                c += 1
        return c

    def number_male(self):
        c = 0
        for student in self.student_list():
            if student.gender == "M":
                c += 1
        return c

    def is_full(self):
        return self.max_students <= len(Placement.objects.filter(course=self))

    def student_list(self):
        placements = Placement.objects.filter(course=self)
        students = []
        for p in placements:
            students.append(p.student)
        return students

    def course_time_string(self):
        if self.is_travel:
            return 'Travel'
        else:
            return self.get_course_type_display()

    def enrolled_students_count(self):
        return len(self.student_list())

    def paid(self):
        return self.cost > 0

    def get_cost_string(self):
        return '$%.0f' % self.cost

    def __str__(self):
        return self.display_name
