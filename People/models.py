from django.db import models
import uuid
import re
from Registrations.models import Placement, Request
from Courses.models import Course

def generateUUID():
    return str(uuid.uuid4())

class Student(models.Model):
    student_id = models.CharField(max_length=36,unique=True,primary_key=True,default=generateUUID)
    first_name = models.CharField(max_length=200,default='')
    last_name = models.CharField(max_length=200,default='')
    grade = models.IntegerField(default=9)
    email = models.CharField(max_length=200,default='')
    common_ground = models.CharField(max_length=200,default='')
    gender = models.CharField(max_length=1,choices=[('F', 'Female'),('M', 'Male')],default='M')
    ford_sayre = models.CharField(max_length=3,choices=[('NO', 'No'),('YES', 'Yes')],default='NO')
    hartford_tech = models.CharField(max_length=2,choices=[('NO', 'No'),('AM', 'Morning'),('PM', 'Afternoon')],default='NO')
    should_ignore = models.BooleanField(default=False)
    no_participate_previous = models.BooleanField(default=False)
    student_leader = models.CharField(max_length=4,choices=[('NO', 'No'),('AM', 'Morning'),('PM', 'Afternoon'),('FULL','Full Day')],default='NO')

    notes = models.CharField(max_length=1000,default='',blank=True)

    class Meta:
        unique_together = ["first_name", "last_name"]

    def full_name(self):
        return '%s %s' % (self.first_name, self.last_name)

    def enrollment_status(self):
        placed_courses = Placement.objects.filter(student=self)
        if len(placed_courses) == 0:
            return "NONE"
        elif len(placed_courses) == 2:
            return "COMPLETE"
        elif len(placed_courses) == 1:
            placement = placed_courses.first()
            if placement.course.course_type == "FULL":
                return "COMPLETE"
            elif placement.course.course_type == "AM":
                if self.ford_sayre == "YES" or self.hartford_tech == "PM":
                    return "COMPLETE"
                else:
                    return "MISSING-PM"
            elif placement.course.course_type == "PM" and self.hartford_tech == "AM":
                return "COMPLETE"
            else:
                return "MISSING-AM"
        else:
            print("ERROR: %s has >2 placements" % self.full_name())
            return "COMPLETE"


    def has_course(self):
        return self.enrollment_status() == "COMPLETE"

    has_course.boolean = True

    def has_requests(self):
        return self.number_of_requests() != 0
    has_requests.boolean = True

    def number_of_requests(self):
        max_request_count = -1
        requests = Request.objects.filter(student=self)
        if len(requests) == 0:
            return 0
        for r in requests:
            if r.request_rank > max_request_count:
                max_request_count = r.request_rank
        return max_request_count + 1

    def requests(self):
        requests = Request.objects.filter(student=self)
        requests_list = []
        for p in requests:
                requests_list.append(p.course)
        return requests_list

    def placements(self):
        placements = Placement.objects.filter(student=self)
        placements_list = []
        for p in placements:
                placements_list.append(p.course)
        return placements_list

    def convert_course_lists(self, list):
        ret_list = []
        for c in list:
            ret_list.append(c.display_name)
        return ret_list

    def signupRestrictionExemption(self):
        if self.ford_sayre == "YES" or self.hartford_tech != "NO":
            return True
        if self.student_leader != "NO":
            return True
        return False
    signupRestrictionExemption.boolean = True;

    def json_representation(self):
        stu = {}
        stu["student_id"] = self.student_id
        stu["first_name"] = self.first_name
        stu["last_name"] = self.last_name
        stu["full_name"] = self.full_name()
        stu["grade"] = self.grade
        stu["ford_sayre"] = self.ford_sayre
        stu["hartford_tech"] = self.hartford_tech
        stu["should_ignore"] = self.should_ignore
        stu["no_participate_previous"] = self.no_participate_previous
        stu["has_course"] = self.has_course()
        stu["has_requests"] = self.has_requests()
        stu["number_of_requests"] = self.number_of_requests()
        stu["requests"] = self.convert_course_lists(self.requests())
        stu["placements"] = self.convert_course_lists(self.placements())
        stu["signupRestrictionExemption"] = self.signupRestrictionExemption()
        stu["student_leader"] = self.student_leader
        stu["notes"] = self.notes
        return stu

    def pub_json_rep(self):
        stu = self.json_representation()
        del stu["placements"]
        del stu["requests"]
        del stu["notes"]
        return stu

    def __str__(self):
        return self.full_name()
