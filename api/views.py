from django.shortcuts import render, HttpResponse, get_object_or_404, get_list_or_404
import json
from People.models import Student
from Courses.models import Course
from Registrations.models import Placement, Request
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from subprocess import call

# Create your views here.

DISABLE_ACTIONS = True;

def returnJSON(j,s=None):
	if s == None:
		s = 200
	return HttpResponse(json.dumps(j), content_type="application/json", status=s)


def API_SUCCESS_RETURN(message="No message!", payload=None, revert_url=None, revert_description=None):
	jxo = {"success": True, "message": message, "revert_url": revert_url, "revert_description": revert_description, "object": payload}
	return returnJSON(jxo)

def API_ERROR_RETURN(message):
	return returnJSON({"success": False, "message": message})

def API_UNKNOWN_ERROR():
	return returnJSON({"success": False, "message": "An unknown error occurred"})

def API_NON_ENDPOINT():
	return returnJSON({"success": False, "message": "Unknown Endpoint"})

def API_NOT_IMPLEMENTED():
	return returnJSON({"success": False, "message": "This endpoint has not been configured"})

def API_DISABLED():
	return API_ERROR_RETURN("Actions are disabled")

def handler404(request):
	return API_NON_ENDPOINT();

def handler500(request):
	return API_UNKNOWN_ERROR();

@login_required
def verify_all_students_complete(request):
	try:
		students = get_list_or_404(Student)
		missing_students = []

		for student in students:
			if len(Request.objects.filter(student=student).order_by('request_rank','course__course_type')) == 0:
				if not student.should_ignore:
					missing_students.append(student)

		if len(missing_students) == 0:
			return API_SUCCESS_RETURN("All students have been completed or marked as ignored.");
		else:
			qty = "Some"
			return API_ERROR_RETURN("%s students have not been completed or marked as ignored." % qty)
	except:
		return API_UNKNOWN_ERROR()

@login_required
def list_incomplete_students(request):
	try:
		students = get_list_or_404(Student)
		missing_students = []

		for student in students:
			if len(Request.objects.filter(student=student)) == 0:
				if not student.should_ignore:
					missing_students.append(student.pk)

		if len(missing_students) == 0:
			return API_ERROR_RETURN("No incomplete students.");
		else:
			return API_SUCCESS_RETURN(None, payload=missing_students)
	except:
		return API_UNKNOWN_ERROR()

@login_required
def reset_placements(request):
	if DISABLE_ACTIONS:
		return API_DISABLED()

	try:
		Placement.objects.all().delete()
		return API_SUCCESS_RETURN("Student placements reset")
	except:
		return API_ERROR_RETURN("An unknown error occurred")

@login_required
def is_ignored(request, student_id=None):
	if student_id == None:
		return API_ERROR_RETURN("No student ID sent")
	else:
		student = get_object_or_404(Student, pk=student_id)
		return API_SUCCESS_RETURN(None, {"ignored":student.should_ignore})

@login_required
def reset_student_placements(request, student_id=None):
	if DISABLE_ACTIONS:
		return API_DISABLED()

	if student_id == None:
		return API_ERROR_RETURN("No student ID sent")
	else:
		try:
			st = get_object_or_404(Student, pk=student_id)
			plcs = Placement.objects.filter(student=st)
			if len(plcs) == 0:
				return API_ERROR_RETURN("No placements to remove")
			plcs.delete()
			return API_SUCCESS_RETURN("Success")
		except:
			return API_ERROR_RETURN("An unknown error occurred")

@login_required
def reset_student_requests(request, student_id=None):
	if DISABLE_ACTIONS:
		return API_DISABLED()

	if student_id == None:
		return API_ERROR_RETURN("No student ID sent")
	else:
		try:
			st = get_object_or_404(Student, pk=student_id)
			requests = Request.objects.filter(student=st)
			if len(requests) == 0:
				return API_ERROR_RETURN("No requests to remove")
			requests.delete()
			return API_SUCCESS_RETURN("Success")
		except:
			return API_ERROR_RETURN("An unknown error occurred")

@login_required
def remove_student_placement(request, student_id=None, course_id=None):
	if DISABLE_ACTIONS:
		return API_DISABLED()

	if student_id == None:
		return API_ERROR_RETURN("No student ID sent")
	elif course_id == None:
		return API_ERROR_RETURN("No course ID sent")
	else:
		try:
			st = get_object_or_404(Student, pk=student_id)
			crs = get_object_or_404(Course, pk=course_id)

			Placement.objects.filter(course=crs,student=st).delete()
			return API_SUCCESS_RETURN("Deleted placement")
		except:
			return API_UNKNOWN_ERROR()

@login_required
def add_student_placement(request, student_id=None, course_id=None):
	if DISABLE_ACTIONS:
		return API_DISABLED()

	if student_id == None:
		return API_ERROR_RETURN("No student ID sent")
	elif course_id == None:
		return API_ERROR_RETURN("No course ID sent")
	else:
		try:
			st = get_object_or_404(Student, pk=student_id)
			crs = get_object_or_404(Course, pk=course_id)

			if crs.is_full():
				return API_ERROR_RETURN("%s is full" % crs.display_name)
			else:
				p, created = Placement.objects.get_or_create(course=crs,student=st)
				if not created:
					return API_ERROR_RETURN("An error occured adding this request\n\n %s may already be enrolled in this course" % st.full_name())
				
				return API_SUCCESS_RETURN("Success")
		except:
			return API_UNKNOWN_ERROR()

@login_required
def add_student_request(request, student_id=None, course_id=None):
	if DISABLE_ACTIONS:
		return API_DISABLED()

	if student_id == None:
		return API_ERROR_RETURN("No student ID sent")
	elif course_id == None:
		return API_ERROR_RETURN("No course ID sent")
	else:
		try:
			st = get_object_or_404(Student, pk=student_id)
			crs = get_object_or_404(Course, pk=course_id)

			print(st)
			print(crs)

			return API_SUCCESS_RETURN("Success")
		except:
			return API_UNKNOWN_ERROR()

@login_required
def ignore_student(request, student_id=None):
	if DISABLE_ACTIONS:
		return API_DISABLED()

	if student_id == None:
		return API_ERROR_RETURN("No student ID sent")
	else:
		student = get_object_or_404(Student, pk=student_id)
		if student.should_ignore:
			return API_ERROR_RETURN("Already ignored")
		else:
			student.should_ignore = True
			student.save()
			return API_SUCCESS_RETURN("Successfull", "/api/student/%s/ignore/false" % student_id)

@login_required
def stop_ignore_student(request, student_id=None):
	if DISABLE_ACTIONS:
		return API_DISABLED()

	if student_id == None:
		return API_ERROR_RETURN("No student ID sent")
	else:
		student = get_object_or_404(Student, pk=student_id)
		if not student.should_ignore:
			return API_ERROR_RETURN("Not ignored")
		else:
			student.should_ignore = False
			student.save()
			return API_SUCCESS_RETURN("Successfull", "/api/student/%s/ignore/true" % student_id)

@login_required
def list_students(request):
	try:
		students = get_list_or_404(Student)
		ret_val = []

		for student in students:
			ret_val.append(student.pk)
		return API_SUCCESS_RETURN(None, payload=ret_val)
	except:
		return API_UNKNOWN_ERROR()

@csrf_exempt
@login_required
def load_student(request, student_id=None):
	s = get_object_or_404(Student, pk=student_id)
	return returnJSON(s.json_representation())

@csrf_exempt
def pub_load_student(request, student_id=None):
	s = get_object_or_404(Student, pk=student_id)
	return returnJSON(s.pub_json_rep())

@login_required
@csrf_exempt
def find_student_by_name(request):
	if request.method == "POST":
		first_name = request.POST.get('first_name', None)
		last_name = request.POST.get('last_name', None)

		if first_name == None:
			return API_ERROR_RETURN("No first name")
		if last_name == None:
			return API_ERROR_RETURN("No last name")

		student = Student.objects.filter(first_name=first_name, last_name=last_name).first()
		if not student:
			return API_ERROR_RETURN("Couldn't find student")
		return API_SUCCESS_RETURN("Found student", payload=student.pk)
	else:
		return API_ERROR_RETURN("Requires POST")

def verify_login(request):
	if request.user.is_authenticated():
		if request.user.is_staff:
			return API_SUCCESS_RETURN("Logged in as %s" % request.user.username)
		else:
			return API_ERROR_RETURN("Your account is not staff")
	else:
		return API_ERROR_RETURN("You are not logged in")

@login_required
def email_class(request, course_id=None):
	if DISABLE_ACTIONS:
		return API_DISABLED()

	course = get_object_or_404(Course, pk=course_id)

	students = course.student_list()

	emails = ""

	room = course.room
	if room == "":
		room = "[ERROR: Couldn't find room]"

	email_string = """Congrats!

You have been selected for the %s March Intensive.

Your meeting will be in %s

- March Intensive Committee""" % (course.display_name, room)

	email_subject = "March Intensive Placement"

	for student in students:
		emails = emails + " " + student.email

	call("echo \"%s\" | mail -s \"%s\"%s" % (email_string, email_subject, emails),shell=True);

	return API_SUCCESS_RETURN("Emails sent")



